Software Invocation Description
===============================

The idea behind the 'Software' invocation description is to define a common way in which multiple software components can be integrated in single workflow.
The definition is composed of a decorator and a configuration file with the necessary parameters of the workflow.

Software decorator
------------------
@software decorator is used to indicate that a certain python function represents the invocation of and external HPC or DA programs in a single workflow.
When a function with the `@software` decorator is called, an (external) program is executed respecting the configuration defined in its configuration file.
The goal of this decorator is to describe the execution of external programs included in a workflow from simple binary executable to complex MPI applications.


Configuration File
------------------
Configuration files can contain different key-values depending on the user's needs. Details of the configuration of the software
execution can be defined in the value of the "execution" key. There the user can define the "type" of the execution and other
necessary configuration parameters the *software* requires.

Next table provides details of some of the supported keys in software configuration files:

    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Key                    | Description                                                                                                                                                        |
    +========================+====================================================================================================================================================================+
    | **execution**          | (Mandatory) Contains all the software execution details such as "type", "binary", "args", etc..                                                                    |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **execution.type**     | (Mandatory) Type of the software invocation. Supported values are 'task', 'workflow', 'mpi', 'binary', 'mpmd_mpi', 'multinode', 'http', and 'compss'.              |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **parameters**         | A dictionary containing *task* parameters.                                                                                                                         |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **prolog**             | A dictionary containing *epilog* parameters.                                                                                                                       |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **epilog**             | A dictionary containing *prolog* parameters.                                                                                                                       |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **constraints**        | Parameters regarding constraints of the software execution.                                                                                                        |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **container**          | Container parameters if the external software is meant to be executed inside a container.                                                                          |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+



Examples
--------

As an example, the following code snippets show how an MPI application execution can be defined using the @software decorator. Users only have to add the software
decorator on top of the function, and provide a 'config_file' parameter where the configuration details are defined:

.. code-block:: python

    from pycompss.api.software import software
    from pycompss.api.task import task

    @software(config_file="mpi_config.json")
    def mpi_execution():
         pass

    def main():
        mpi_execution()


And inside the configuration file the type of execution (mpi), and its properties are set. For example, if the user wants to run an MPI job with two processes using
'mpirun' command, the configuration file (**"mpi_config.json"** in this example) should look like as follows:

.. code-block:: JSON

    {
      "execution" : {
        "type":"mpi",
        "runner": "mpirun",
        "binary":"my_mpi_app.bin",
        "processes": 2,
        }
    }


It is also possible to refer to task parameters and environment variables from the configuration file. Properties such as `working_dir` and `args` ('args' strings are command line arguments to be passed to the 'binary') can contain this kind of references. In this case, the task parameters should be surrounded by curly braces. For example, in the
following example, 'work_dir' and 'param_d' parameters of the python task are used in the 'working_dir' and 'args' strings respectively. An the number of MPI processes are got form an environment variable. Moreover, epilog and prolog definitions, as well as
the number of computing units is added as a constraint, to indicate that every MPI process will have this requirement (run with 2 threads):

Task definition and invocation:

.. code-block:: python

    from pycompss.api.software import software
    from pycompss.api.task import task

    @software(config_file="mpi_w_args.json")
    def mpi_with_args(work_dir, param_d, out_tgz):
         pass

    def main():
    working_dir = "/tmp/mpi_working_dir/"
    arg_value = 1001
    mpi_with_args(working_dir, ar_value, "output.tgz")


Configuration file ("mpi_w_args.json"):

.. code-block:: JSON

    {
      "execution" : {
        "type":"mpi",
        "runner": "mpirun",
        "processes" : "$MPI_PROCS",
        "binary":"my_binary.bin",
        "working_dir": "{{work_dir}}",
        "args": "-d {{param_d}}"
      },
      "parameters" : {
        "param_d": "IN",
        "work_dir": "DIRECTORY_OUT",
        "out_tgz": "FILE_OUT"
      }
      "prolog": {
        "binary": "mkdir",
        "args": "{{work_dir}}"
      },
      "epilog": {
        "binary":"tar",
        "args":"zcvf {{out_tgz}} {{work_dir}}"
      },
      "constraints":{
        "computing_units": 2
      }

    }


Another example can be when the external program is expected to run within a container. For that, the user can add the `container` configuration to the JSON file
by specifying its 'engine' and the 'image'. At the time of execution, the Runtime will execute the given program within the container. For example, in order to run a
simple 'grep' command that searches for a pattern (e.g. an 'error' ) in the input directory recursively within a Docker container, the task definition and the configuration file should
be similar to the examples below:

Task definition:

.. code-block:: python

    from pycompss.api.parameter import FILE_IN
    from pycompss.api.software import software
    from pycompss.api.task import task

    @software(config_file="container_config.json")
    def task_container(in_directory, expression):
         pass

    def main():
       task_container('/tmp/my_logs/', 'Error')


Configuration file ("container_config.json"):

.. code-block:: JSON

    {
      "execution" : {
        "type":"binary",
        "binary": "grep",
        "args": "{{expression}} {{in_directory}} -ir"
        },
      "parameters":{
        "in_directory": "DIRECTORY_IN",
        "expression": "IN"
      },
      "container":{
        "engine": "DOCKER",
        "image": "ubuntu:20.04"
      }
    }



For more detailed information about the @software decorator of PyCOMPSs please see the `documentation`_.


.. _documentation: https://compss.readthedocs.io/en/stable/Sections/02_App_Development/02_Python/01_1_Task_definition/Sections/06_Other_task_types/11_Software_decorator.html
