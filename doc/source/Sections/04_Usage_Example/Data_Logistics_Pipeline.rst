Implementing Data Logistics Pipeline
====================================

Data movements in eFlows4HPC minimal workflow are orchestrated by Data Logistics Service and defined
within it as Airflow Pipelines. The pipelines formally are Direct Acyclic Graphs (DAGs) and are 
defined programmatically with Python. 

Each DAG definition is comprised of set of tasks and additional metadata. The metadata can be used to, e.g., 
orchestrate periodic data movements. The tasks are then executed by Airflow workers. The most common type 
of tasks are Operators. Airflow provides a wide range of Operators to interact with different data services 
and storages. It is also possible to create own operators. 

Following will provide a short introduction to Data Logistics Pipelines based on example of eFlows4HPC minimal
workflow. The complete source code of minimal workflow pipeline can be found in repository_. The workflow is
build following the principle of Extract Transform Load (ETL) and uses Airflow taskflow API to define DAG. 

DAG Definition
--------------

The structure of DAG is defined as follows:

::


    @dag(default_args=default_args, schedule_interval=None, start_date=days_ago(2), tags=['example'])
    def taskflow_example():

        @task
        def setup(**kwargs):
           ....

        @task(multiple_outputs=True)
        def extract(conn_id, **kwargs):
           ....

        ....

        conn_id = setup()
        data = extract(conn_id)
        files = transform(data)
        ucid = load(connection_id = conn_id, files=files)
        remove(conn_id=ucid)

    dag = taskflow_example()

The DAG is defined as Python annotated function ``taskflow_example``. The submethods annotated with ``@task`` are Operators, finally
the dependencies between tasks emerge from order of function calls in ``taskflow_example`` method. 

Data Movement Tasks 
-------------------
The minimal workflow encompasses following data movements:
- download from B2SHARE repository,

- upload to target system with SCP/SFTP,

- upload computation results to B2SHARE repository. 

The code of accessing and downloading from B2SHARE can be seen in repository_. Objects in B2SHARE comprise of an id, set of metadata and list of files. 
To identify which object needs to be downloaded, the object id needs to be passed to DAG as ``oid`` parameter. The workflow will then locate the object 
in the B2SHARE, retrieve the list of its files (``extract`` task), and download the files to local storage ``transform`` task. There is also an example of 
streaming pipeline (which does not download to local storage but rather directly to target location), it can be found in repository_. 

Next step in data movement is to use SCP to upload the files from B2SHARE to target system. This is done in ``load`` task. The task uses functionality 
provided by Airflow to access SSH/SCP systems. 

Connection setup
----------------
The credentials needed to access storages are passed to the DAG. Based on their content a temporary Airflow connection is created, used by Data Movement Tasks 
and removed subsequently. The connection management is taken care of by ``setup`` and ``remove`` tasks. 


Closing remarks
---------------
Please review the examples in repository_ to gain understanding how the data movements are realized. There are examples of upload/download to remote repository, 
streaming, accessing storages through SCP/SFTP or HTTP. 

The repository also includes set of tests and mocked tests to verify the correctness of the pipelines. 

For local testing, you can use airflow standalone setup. Please refer to Airflow documentation_ for that. 


.. _repository: https://gitlab.jsc.fz-juelich.de/eflows4hpc-wp2/data-logistics-service/-/blob/main/dags/taskflow.py
.. _documentation: https://airflow.apache.org 