Data Catalog
============

Following describes the architecture of eFlows4HPC Data Catalog. The service
will provide information about data sets used in the project. The catalog will
store info about locations, schemas, and additional metadata.


Main features:

* keep track of data sources used in the project (by workflows)
* enable registration of new data sources
* provide user-view as well as simple API to access the information

The Data Catalog is mainly developed at FZJ. The source code for stable versions can be found in Repository_. 
This also includes a description of architecture_.

The running istance with content is hosted on HDF Cloud and can be accessed at Address_.

Data Catalog offers API_ to access and manipulate its content.

.. _Repository: https://github.com/eflows4hpc/datacatalog
.. _architecture: https://github.com/eflows4hpc/datacatalog/blob/master/arch/arch.adoc
.. _Address: https://datacatalog.fz-juelich.de/
.. _API: https://datacatalog.fz-juelich.de/docs
