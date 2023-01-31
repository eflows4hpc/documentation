Data Logistics Service
======================

The Data Logistics Service (DLS) is responsible for data movements part of the workflows developed in the project.

The service is based on Apache Airflow_. The project specific extensions can be found in the project repository_.

From the user perspective, the most important part of the service is the definition of data movements (pipelines).
Some examples (e.g. minimal workflow) of these are provided in the dagrepo_. The pipelines defined in this repository are automatically deployed to the production instances of DLS.

A good starting point for defining your
own pipelines is the original documentation_. Note that the pipelines are defined in the Python programming language
and can execute shell scripts. This means that if the users already have their data movement solution based on scripts or
Python programs, they can easily be migrated to the Data Logistics Service to obtain a running environment with monitoring, retires upon failure, etc.

There is an instance of the data logistics service hosted in HDF could which can be accessed_.



.. _Airflow: https://airflow.apache.org
.. _repository: https://github.com/eflows4hpc/data-logistics-service
.. _dagrepo: https://github.com/eflows4hpc/dls-dags
.. _documentation: https://airflow.apache.org/docs/apache-airflow/stable/index.html
.. _accessed: https://datalogistics.eflows4hpc.eu/
