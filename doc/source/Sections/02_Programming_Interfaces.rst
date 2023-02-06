Programming Interfaces for integrating HPC and DA/ML workflows
==============================================================

The evolution of High-Performance Computing (HPC) platforms enables the design and execution of progressively more complex and larger workflow applications in these systems. The complexity comes not only from the number of elements that compose a workflow but also from the type of computations performed. While traditional HPC workflows include simulations and modeling tasks, current needs require in addition Data Analytic (DA) and artificial intelligence (AI) tasks.
However, the development of these workflows is hampered by the lack of proper programming models and environments that support the integration of HPC, DA, and AI. Each of these workflow phases are developed using dedicated frameworks for the specific problem to solve. However, to implement the overall workflow, developers have to deal with programming large glue code to integrate the execution of the different frameworks executions in a single workflow.

eFlows4HPC proposes a programming interface to try to reduce the effort required to integrate different frameworks in a single workflow. This integration can be divided in two parts:

- **Software Invocation Management:** It includes the actions required to execute
  an application with a certain framework. This can be invoking just a single binary,
  a MPI application or a model training with a certain ML framework.

- **Data Integration:** In includes the transformations that the data generated
  by a framework has to be applied to be used by another framework. This
  can include transformations like transpositions, filtering or data distribution.


.. _fig_programming_interfaces:
.. figure:: Figures/programming_interfaces.png
    :figwidth: 50 %
    :alt: Interfaces to integrate HPC/DA/ML.
    :align: center

    Interfaces to integrate HPC/DA/ML.


The proposed interface aims at declaring the different software invocations required in a workflow as simple python functions. This functions will be annotated by two decorators :

- **@software** to describe the type of execution to be performed when the function
  is invoked from the main code

- **@data_transformation** to indicate the required data transformations that a
  parameter of the invocation has to apply to be compatible with the input of expected execution.


During the first iteration, we defined the software invocation descriptions and extended the PyCOMPSs programming model and runtime.ç
In the following version of the eFlows4HPC framework, we included the definition of the data transformations and
their implementations.

.. toctree::
    :maxdepth: 1

    02_Programming_Interfaces/Software_Description
    02_Programming_Interfaces/Data_Transformation
