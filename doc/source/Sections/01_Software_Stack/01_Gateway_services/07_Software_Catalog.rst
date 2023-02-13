Software Catalog
================
The Software Catalog is a git repository to store the description of the software to be used in computational HPC workflows using the eFlows4HPC methodology. The eFlows4HPC Software Catalog can be found in this repository_.

Repository structure
--------------------

Software descriptions have to be included inside this repository according to the following structure. The different software descriptions are located as a subfolder of the ``packages`` directory. This includes the installation description as a Spack package description_ and the `Software invocation description <../../02_Programming_Interfaces/Software_Description.rst>`_.

.. code:: bash

  software-catalog
    |- packages
    |    |- software_1
    |    |    |- package.py		    # Installation description following the Spack package format
    |    |    |- invocation.json  # Description of the software invocation
    |    |       ...
    |    |- software_2
    |          ....
    |- cfg				     # Spack configuration used by the Image Creation Service
    |
    |- repo.yaml			 # Spack description of this repository


Including new software
----------------------

To include new  software in the repository, create a fork of the repository. Inside the packages folder create a new folder with the name of the software. This folder should contain the description of the new software including at least the Spack package description_ and `Software invocation description <../../02_Programming_Interfaces/Software_Description.rst>`_.

Finally, create a create pull request with the branch of the newly added software. This pull request will be reviewed an  merged to the repository.

.. _repository: https://github.com/eflows4hpc/software-catalog
.. _description: https://spack.readthedocs.io/en/latest/packaging_guide.html
