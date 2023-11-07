Workflow Execution Service
==========================

The Workflow Execution Service is a RESTful web service that provides a way for end users to execute workflows using a simple rest API
This component is developed specifically for the eFlows4HPC project.

This service interacts with Alien4Cloud and Yorc to list and trigger applicative workflows and with Hashicorp Vault to manage users access credentials.

The source code can be found in the project repository_.

Installation
------------

The easiest way to install this service is to use docker.
A docker image is automatically published with latest changes under the name ``ghcr.io/eflows4hpc/hpcwaas-api:main``.


Running the Service using docker
--------------------------------

Please refer to the help of the hpcwaas-api container to know how to run it.

.. code:: bash

    docker run ghcr.io/eflows4hpc/hpcwaas-api:main --help

Using the Service API
---------------------
The HPCWaaS execution API can be invoked usign different tools:

It can be directly accesssed through its HTTP interface with tools like ``curl`` or any programming language. Please refer to the repository documentation_ for a detailed description of the different
endpoints of this API. The basic usage of this API is the following:

First you need to setup your SSH credentials using the `Create an SSH Key Pair for a given user endpoint <https://github.com/eflows4hpc/hpcwaas-api/blob/main/docs/rest-api.md#create-an-ssh-key-pair-for-a-given-user>`_.
By calling this endpoint the API will create a new SSH key pair and store it into a vault you will receive in return of this call
the public key. You will never get or even see the private key.
Add this public key as an authorized key for your HPC user account in order to let transfer data to your user account and run
jobs for you in an automated way.

Then you can use the `list available workflows endpoint <https://github.com/eflows4hpc/hpcwaas-api/blob/main/docs/rest-api.md#list-available-workflows>`_
to get the list of endpoints you can access. You can then `trigger a workflow execution <https://github.com/eflows4hpc/hpcwaas-api/blob/main/docs/rest-api.md#trigger-a-workflow-execution>`_.
And finally `monitor the workflow execution <https://github.com/eflows4hpc/hpcwaas-api/blob/main/docs/rest-api.md#monitor-a-workflow-execution>`_.

A Command Line Interface (CLI) is also available to interact with the service. Visit the `HPCWaaS API release page on GitHub <https://github.com/eflows4hpc/hpcwaas-api/releases>`_ to download a binary version of
the ``waas`` CLI that is compatible with your computer.

Alternatively, a Docker image (ghcr.io/eflows4hpc/hpcwaas-api:main-cli) containing the CLI can also be obtained.
To utilize the Docker image, the following command can be executed in the terminal:

.. code-block:: bash

    docker run -ti --rm ghcr.io/eflows4hpc/hpcwaas-api:main-cli help

This is equivalent to executing:

.. code-block:: bash

    ./waas help

For a more detailed usage of the CLI please refer to :ref:`section_workflow_execution`.

There are running instances of this API on both Juelich and BSC clouds, ask to the team (eflows4hpc@bsc.es) for an access to the API.

.. _documentation: https://github.com/eflows4hpc/hpcwaas-api/blob/main/docs/rest-api.md
.. _repository: https://github.com/eflows4hpc/hpcwaas-api
.. _registry: https://github.com/eflows4hpc/hpcwaas-api/pkgs/container/hpcwaas-api
