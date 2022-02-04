dataClay
========

`dataClay`_ is a distributed object store with active capabilities. It is designed to hide distribution details while taking advantage of the underlying infrastructure, be it an HPC cluster or a highly distributed environment such as edge-to-cloud. 
Objects in dataClay are enriched with semantics, giving them a structure as well as the possibility to attach arbitrary user code to them. In this way, dataClay enables applications to store and access objects in the same format they have in memory (Python or Java objects), also allowing them to execute object methods within the store to exploit data locality. This active capability minimizes data transfers, as only the results of the computation are transferred to the application, instead of the whole object.

dataClay implements the Storage Runtime Interface that `PyCOMPSs`_ can use to enhance data locality of parallalel and distributed 
applications. This implementation hints the runtime scheduler to assign tasks that access data managed by dataClay to the nodes containing 
that data, and allows to avoid the cost of serializing this data when it is accessed from several tasks.

Some useful links for more detailed information:

1. Source code: https://github.com/bsc-dom

2. Examples: https://github.com/bsc-dom/dataclay-demos

3. User manual (see Chapter 7 for installation instructions): https://www.bsc.es/research-and-development/software-and-apps/software-list/dataclay/documentation

4. Docker Hub repository: https://hub.docker.com/u/bscdataclay/



.. _dataClay: https://dataclay.bsc.es/
.. _PyCOMPSs: https://compss-doc.readthedocs.io/en/stable/
