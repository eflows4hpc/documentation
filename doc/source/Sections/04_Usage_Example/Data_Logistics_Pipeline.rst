Implementing a Data Logistics Pipeline
======================================

Data movements in the eFlows4HPC Workflow-as-a-Service are orchestrated by the Data Logistics Service and defined as Airflow Pipelines. The pipelines are formally Direct Acyclic Graphs (DAGs) and are defined programmatically using Python.

Each DAG definition consists of a set of tasks and additional metadata. The metadata can be used, for example, to orchestrate periodic data movements. The tasks are then executed by Airflow workers. The most common type of tasks are Operators. Airflow provides a wide range of Operators to interact with different data services and storages. It is also possible to create custom operators.

The following is a brief introduction to Data Logistics Pipelines using the eFlows4HPC Pillar 1 workflow as an example. The complete source code of the workflow pipeline can be found in repository_. The workflow is built on the principle of Extract Transform Load (ETL) and uses the Airflow taskflow API to define a DAG.

DAG Definition: HTTP-based transfer
-----------------------------------

The stage-in of the data in Pillar I is fairly straightforward. The source of the data is a B2DROP repository that provides HTTP access. The destination is an HPC system accessed via SSH.

::

    @dag(default_args=default_args, schedule_interval=None, start_date=days_ago(2), tags=['wp4', 'http', 'ssh'])
    def plainhttp2ssh():

        @task
        def stream_upload(connection_id, **kwargs):
            params = kwargs['params']
            force = params.get('force', True)
            target = params.get('target', '/tmp/')
            url = params.get('url', '')
            if not url:
                print('Provide valid url')
                return -1

            print(f"Putting {url} --> {target}")
            ssh_hook = get_connection(conn_id=connection_id, **kwargs)

            with ssh_hook.get_conn() as ssh_client:
                return http2ssh(url=url, ssh_client=ssh_client, remote_name=target, force=force)

        setup_task = PythonOperator(python_callable=setup, task_id='setup_connection')
        a_id = setup_task.output['return_value']
        cleanup_task = PythonOperator(python_callable=remove, op_kwargs={'conn_id': a_id}, task_id='cleanup')

        setup_task >> stream_upload(connection_id=a_id) >> cleanup_task

    dag = plainhttp2ssh()



The DAG is defined as a Python annotated function ``plainhttp2ssh``. The submethods (only one in this case) are annotated with ``@task`` are Operators, finally the dependencies between tasks are defined with help of ``>>`` operator.



Data Movement Tasks
-------------------
The workflow includes the following data movements:

- download from B2DROP repository,

- upload to the target system using SCP/SFTP.

The ``http2ssh`` method streams the data directly to the target location, without an intermediate storage on the DLS server. Although, the transfer pipeline is implemented with B2DROP in mind, any data source that provides HTTP-based access can be used here. The ``force`` parameter passed to the pipeline defines what to do if the requested data are already exist at the target location (overwrite or not). This is useful if the
workflow needs to be run multiple times.


Connection setup
----------------
The credentials required to access storages are passed to the DAG through external component ``vault``. Based on their contents a temporary Airflow connection is created, used by Data Movement Tasks and then removed. The connection management is taken care of by ``setup`` and ``remove`` tasks. The data movement method
is provided with ``connection_id`` that is dynamically created for the particular data transfer.


.. _section-image-transfer:

DAG Definition: Singularity image transfer
------------------------------------------
After the successful stage-in of the data, a computation step follows. The computations in Pillar I workflow are performed using Singularity containers. This requires a Singularity image to be present on the target machine. The HPC nodes usually don't have Internet access, thus the image needs to be uploaded to the right place before the computation happens. The following code shows how such a transfer can be performed.

::

    @dag(default_args=default_args, schedule_interval=None, start_date=days_ago(2), tags=['example'])
    def transfer_image():

        @task
        def stream_upload(connection_id, **kwargs):
            params = kwargs['params']
            force = params.get('force', True)
            target = params.get('target', '/tmp/')
            image_id = params.get('image_id', 'wordcount_skylake.sif')
            target = os.path.join(target, image_id)
            url = f"https://bscgrid20.bsc.es/image_creation/images/download/{image_id}"

            ssh_hook = get_connection(conn_id=connection_id, **kwargs)

            with ssh_hook.get_conn() as ssh_client:
                return http2ssh(url=url, ssh_client=ssh_client, remote_name=target, force=force)

        setup_task = PythonOperator(python_callable=setup, task_id='setup_connection')
        a_id = setup_task.output['return_value']
        cleanup_task = PythonOperator(python_callable=remove, op_kwargs={'conn_id': a_id}, task_id='cleanup')

        setup_task >> stream_upload(connection_id=a_id) >> cleanup_task


    dag = transfer_image()


This pipeline is almost identical to the previous one as the images are downloaded from the eFlows4HPC image service which provides HTTP-based access and uploaded to the target location using SSH. The only difference is the use of the ``image_id`` parameter instead of the full ``url`` as in the previous example.


Final remarks
---------------
Please review the examples in the repository_ to gain understanding how the data movements are realized. There are examples of upload/download to remote repository, streaming, accessing storages through SCP/SFTP or HTTP.

The repository also includes a set of tests and mocked tests to verify the correctness of the pipelines.

For local testing, you can use airflow standalone setup. Please refer to Airflow documentation_ for more information.

If you intend to use eFlows4HPC resources accessed via SSH, reuse ``setup_task`` and ``cleanup_task``.

The data movements are part of the overall workflow and are executed via the TOSCA descriptions (see :ref:`dlstosca` for more details). For testing purposes, however, you can start the pipelines directly either via the Airflow UI or via API calls.

::

        curl -X POST -u airflowuser:airflowpass \
                -H "Content-Type: application/json" \
                --data '{"conf": {"image_id": "wordcount_skylake.sif", "target": "/tmp/", "host": "sshhost", "login": "sshlogin", "vault_id": "youruserid"}}' \
                https://datalogistics.eflows4hpc.eu/api/v1/image_transfer/dagRuns


If you don't have credentials registered in vault (or are using local standalone Airflow) you can provide ssh credentials in the API call:

::

         curl -X POST -u airflowuser:airflowpass \
                -H "Content-Type: application/json" \
                --data '{"conf": {"image_id": "wordcount_skylake.sif", "target": "/tmp/", "host": "sshhost", "login": "sshlogin", "key": "sshkey"}}' \
                http://localhost:5001/api/v1/image_transfer/dagRuns



.. _repository: https://github.com/eflows4hpc/dls-dags
.. _documentation: https://airflow.apache.org
