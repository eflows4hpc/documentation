Enabling HPC Ready Container Image Creation
===========================================

In the previous section, we have seen how to implement the computational workflow with PyCOMPSs. To enable the deployment of this workflow as containers we have to indicate what software is required for the execution of this service. As we have seen in previous section, the reduced order model computation requires Kratos Multiphysics for the FOM and ROM simulations, dislib for rSVD and results comparison and COMPSs as runtime system to manage PyCOMPSs workflows. These requirements have to be defined as a simplified Spack environment (`spack.yml`) inside the workflow folder stored in the Workflow Registry as shown in :numref:`spack_description`. Developers just need to indicate the required software package name and optionally specify the version and variants for this software. For instance, this workflow requires `Kratos` version `9.1.4` with the `app` variant which indicates the Kratos applications to include in the compilation. No other Spack environment information must be included in this description, the rest of options of the spack environment will be included at the image creation process.

.. code-block:: yaml
    :name: spack_description
    :caption: Workflow Software requirements as simplified spack environment.

    spack:
            specs:
                    - compss
                    - py-dislib
                    - kratos@9.1.4 apps=LinearSolversApplication,FluidDynamicsApplication,StructuralMechanicsApplication,ConvectionDiffusionApplication,RomApplication

The description of the software packages indicated in `spack.yml` must be included in the `Software Catalog  <../01_Software_Stack/01_Gateway_services/07_Software_Catalog.rst>`_ or `supported by Spack <https://spack.readthedocs.io/en/latest/package_list.html>`_. This description must follow the Spack package description_ format. It is a python class which defines the packaging type (autotools, cmake, python, etc.), the location to download the sources, available versions, software dependencies, and other options depending on the packaging type. For instance, :numref:`spack_description` shows how this description has been implemented for COMPSs. It uses the basic packaging type (extends `Package`) and the installation procedure is described by implementing the `install` method. More examples can be found in the Software Catalog repository_.

.. code-block:: python
    :name: compss_spack_description
    :caption: Spack package description for COMPSs.

    class Compss(Package):
        """COMP Superscalar programming model and runtime."""

        url      = "https://compss.bsc.es/repo/sc/stable/COMPSs_2.10.tar.gz"
        version('2.10', sha256='0795ca7674f1bdd0faeac950fa329377596494f64223650fe65a096807d58a60', preferred=True)
        ...

        # dependencies.
        depends_on('python')
        depends_on('openjdk')
        depends_on('boost')
        depends_on('libxml2')
        ...

        def install(self, spec, prefix):
            install_script = Executable('./install')
            install_script('-A', '--only-python-3', prefix.compss)

        def setup_run_environment(self, env):
            env.set('COMPSS_HOME', self.prefix.compss)
            env.prepend_path('PATH', self.prefix.compss + '/Runtime/scripts/user')

Once the workflow software requirements and the software package description have been included in the Workflow Registry and Software Catalog respectively, we can start to create the container images for this workflow. To do it, developers have to request it to the Container Image Creation service using the command line interface (CLI). :numref:`cic_request` and :numref:`request_json` shows the command and JSON file of the request for creating the ROM workflow container image for the MareNostrum4. This supercomputer has a `skylake_avx512` architecture and supports Singularity containers.


.. code-block:: bash
    :name: cic_request
    :caption: Container Image Creation CLI command for ROM image creation request for MN4.

    $ image_creation> ./cic_cli user pass https://bscgrid20.bsc.es build rom_for_MN4.json
    Response:
    {"id":"f1f4699b-9048-4ecc-aff3-1c689b855adc"}


.. code-block:: json
    :name: request_json
    :caption: ROM image creation request for MN4 supercomputer.

    {
         "machine": {
              "platform": "linux/amd64",
              "architecture": "skylake_avx512",
              "container_engine": "singularity"
         },
         "workflow":"rom_pillar_I",
         "step_id" :"reduce_order_model"
    }


More details about the Container Image Creation service can be found in `this link <../01_Software_Stack/01_Gateway_services/06_Container_Image_Creation.rst>`_.


.. _repository: https://github.com/eflows4hpc/software-catalog
.. _description: https://spack.readthedocs.io/en/latest/packaging_guide.html
