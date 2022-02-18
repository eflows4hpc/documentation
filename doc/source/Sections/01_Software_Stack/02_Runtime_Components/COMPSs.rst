PyCOMPSs
========

`COMPSs`_ is a task-based programming model which provides parallel execution of applications on distributed systems.
Its model abstracts the application from the underlying distributed infrastructure, allowing it to be portable between
infrastructures with diverse characteristics. PyCOMPSs is the Python binding of COMPSs.

When developing with PyCOMPSs, distribution of the data, task scheduling, data dependency between tasks, and fault tolerance issues are hidden to the user
and are the responsibilities of the COMPSs Runtime. The COMPSs Runtime is also able to react to task failures and exceptions in order to adapt the
behaviour accordingly.

Programs written in a sequential way can be converted to PyCOMPSs applications simply by adding 'task' decorators
to the functions that can be executed in parallel with other tasks. `These sample applications`_ show how to tag tasks to-be-parallelized.

Tasks in PyCOMPSs can be of different granularity, from fine grain tasks with short duration to invocation to external binaries
(including MPI applications) that last longer time. This flexibility enables PyCOMPSs to support the development on workflows with heterogeneous task types.

Some useful links for more detailed information:

1. `Source code`_.
2. `Installation`_.
3. `PyCOMPSs Tutorials`_.
4. `PyCOMPSs Syntax Reference`_.


.. _COMPSs: http://compss.bsc.es
.. _These sample applications: https://compss.readthedocs.io/en/stable/Sections/07_Sample_Applications/02_Python.html
.. _`Source code`: https://github.com/bsc-wdc/compss
.. _`Installation`: https://compss.readthedocs.io/en/stable/Sections/00_Quickstart.html#install-compss
.. _`PyCOMPSs Tutorials`: https://compss.readthedocs.io/en/stable/Sections/10_Tutorial/02_PyCOMPSs.html
.. _`PyCOMPSs Syntax Reference`: https://compss.readthedocs.io/en/stable/Sections/02_App_Development/02_Python.html
