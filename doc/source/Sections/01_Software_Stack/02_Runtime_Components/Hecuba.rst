Hecuba
======

`Hecuba`_  is a set of tools and interfaces that implement a simple and efficient access to data stores for big data applications. 
One of the goals of Hecuba is to provide programmers with an easy and portable interface to access data. This interface is 
independent of the type of system and storage used to keep data, enhancing the portability of the applications. 
Using Hecuba, the applications can access data like regular objects stored in memory and Hecuba translates 
the code at runtime into the proper code, according to the backing storage used in each scenario.
The current implementation of Hecuba implements this interface for Python and C/C++ applications that store data in memory or `Apache Cassandra`_. 

Hecuba also implements the Storage Runtime Interface that `PyCOMPSs`_ can use to enhance data locality of parallalel and distributed 
applications. This implementation hints the runtime scheduler to assign tasks that access Hecuba-managed data to the nodes that contain that data, and allows to avoid the cost of serializing this data when it is accessed from several tasks.

Some useful links for more detailed information:

1. Source code and installation instructions: https://github.com/eflows4hpc/hecuba
2. Manual: https://github.com/eflows4hpc/hecuba/wiki/1:-User-Manual


.. _Hecuba: https://github.com/eflows4hpc/hecuba
.. _Apache Cassandra: https://cassandra.apache.org/_/index.html
.. _PyCOMPSs: https://compss-doc.readthedocs.io/en/stable/

