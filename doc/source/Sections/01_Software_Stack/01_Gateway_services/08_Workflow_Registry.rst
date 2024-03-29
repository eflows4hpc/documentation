Workflow Registry
===================

The Workflow Registry is a git repository that stores the Workflow descriptions using the eFlows4HPC methodology. This description consist of at least the TOSCA description of the workflow, the code of the their different steps and their required software per step. The eFlows4HPC Workflow Registry can be found in this repository_.


Repository structure
--------------------
Workflow descriptions have to be included inside this repository according to the following structure. Each workflow description should contain a ``tosca`` folder with the TOSCA topology with the relationship of the PyCOMPSs executions and the required image creations for the different steps, data pipelines and HPC environments and one or several folders for PyCOMPSs application as workflow step.

.. code:: bash

  workflow-registry
    |- workflow_1
    |    |- tosca
    |    |    |- types.yml         # TOSCA description of the different components involved in the workflow
    |    |       ...
    |    |- step_1
    |    |    |- spack.yml         # Software requirements for this workflow step as a Spack environment specification
    |    |    |- src               # PyCOMPSs code of the workflow step
    |    |       ...
    |    |- step_2
    |         ....
    |- workflow_2
    |	...


Including new Workflows
-----------------------
To include new workflows in the repository, first create a new fork of the repository. Inside the forked repository, create a new directory with the name of your workflow. This directory should include the workflow description with a sub-folder for the TOSCA description and the different workflow steps. Each workflow step correspond to a PyCOMPSs code which must be executed in a HPC cluster. The description of the steps should include the software requirements as a Spack environment_ and the PyCOMPSs code.

Finally, create a pull request with the new workflow description. This pull request will be reviewed and included in the repository.

.. _repository: https://github.com/eflows4hpc/workflow-registry
.. _environment: https://spack.readthedocs.io/en/latest/environments.html
