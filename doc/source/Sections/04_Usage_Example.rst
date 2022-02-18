=============
Usage Example
=============

This section describe a minimal usage example on how to implement, deploy and execute
a workflow using the eFlows4HPC Software Stack. This example workflow consists of
two main steps:

  - a data logistic pipeline, where the input data is moved from an EU Data repository to the parallel file system of a supercomputer where it will be processed in the second step.
  - a PyCOMPSs workflow, where an word-count computation is parallelized across the nodes of an HPC facility using a task-based programming model .

The deployment and execution of these two steps are described as a TOSCA application
using the HPCWaaS methodology.

In this first version of the workflow, we have assumed that the required software
and the access credentials are already deployed in the infrastructure. Next versions
of this document will include how to do it with the eFlows4HPC Software Stack.

Next sections provide more details about how the different steps are implemented.

.. toctree::
   :maxdepth: 1

   04_Usage_Example/Data_Logistics_Pipeline
   04_Usage_Example/PyCOMPSs_workflow
   04_Usage_Example/TOSCA_Description
