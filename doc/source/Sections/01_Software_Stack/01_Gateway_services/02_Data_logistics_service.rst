Data Logistics Service
======================

The Data Logistics Service is responsible for data movements part of the workflows developed in the project. 

The service is based on Apache Airflow_. The project specific extensions and data pipelines formalizing the 
data movements can be found in the project repository_. 

From the user perspective, the most important part of the service are the definitions of data movements (pipelines). 
Some examples (e.g. minimal workflow) of those are provided in the repository_. A good starting point for defining
own pipelines is the original documentation_. Please note that the pipelines are defined in Python programming language
and can execute shell scripts. 
That means that if the users already have their own solution for data movements which are based on scripts or 
Python programs they can easily be moved to the Data Logistics Service to obtain a running environment with 
monitoring, retires upon failure, etc. 

There is a testing instance of the data logistics service hosted in HDF could which can be accessed_. 



.. _Airflow: https://airflow.apache.org
.. _repository: https://github.com/eflows4hpc/data-logistics-service
.. _documentation: https://airflow.apache.org/docs/apache-airflow/stable/index.html
.. _accessed: http://zam10220.zam.kfa-juelich.de:7001
