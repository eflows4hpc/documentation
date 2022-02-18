Execution API
=============

The execution API is still under active development and is subject to changes.
Please refer to the repository documentation_ for a detailed description of the current status of the different
endpoints of this API.

A Command Line Interface (CLI) allows to interact with the service. It is available as a container.
Please refer to the help of the ``waas`` container to know how to run it.

.. code:: bash

    docker run ghcr.io/eflows4hpc/hpcwaas-api:main-cli --help

The API can also be accessed directly through its HTTP interface with tools like ``curl`` or any programming language.

There is a running instance on Juelich cloud, ask to the team for access to the API.

Basic usage
-----------

First you need to setup your SSH credentials using the `Create an SSH Key Pair for a given user endpoint <https://github.com/eflows4hpc/hpcwaas-api/blob/main/docs/rest-api.md#create-an-ssh-key-pair-for-a-given-user>_`.
By calling this endpoint the API will create a new SSH key pair and store it into a vault you will receive in return of this call
the public key. You will never get or even see the private key.
Add this public key as an authorized key for your HPC user account in order to let transfer data to your user account and run
PyCOMPS jobs for you in an automated way.

Then you can use the `list available workflows endpoint <https://github.com/eflows4hpc/hpcwaas-api/blob/main/docs/rest-api.md#list-available-workflows>`_
to get the list of endpoints you can access.

You can then `trigger a workflow execution <https://github.com/eflows4hpc/hpcwaas-api/blob/main/docs/rest-api.md#trigger-a-workflow-execution>`_.

And finally `monitor the workflow execution <https://github.com/eflows4hpc/hpcwaas-api/blob/main/docs/rest-api.md#monitor-a-workflow-execution>`_.

.. _documentation: https://github.com/eflows4hpc/hpcwaas-api/blob/main/docs/rest-api.md
