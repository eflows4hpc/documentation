EDDL
====

EDDL is an open-source software for deployment of neural network models on different target devices. EDDL allows the instantiation of many of the current neural network topologies, including CNNs, MLP, and Recurrent networks, performing training and inference. Training can be deployed in an HPC system by the use of COMPSs and MPI/NCCL. For this, a distributed training algorithm is used. 

Inside EDDL, a Tensor class is provided with all required tensor manipulation functions needed in neural networks. Currently, EDDL runs on CPU systems, GPU (NVIDIA devices) systems and FPGAs (Xilinx devices). EDDL allows a transparent use of devices.

EDDL is written in C++. A python wrapper is available. EDDL is available on github_.

Complete documentation_ (description, usage, API, examples) is available.

Installation
------------

EDDL allows different methods for installation. The simplest one is by using conda:

::

   conta install -c deephealth eddl-cpu

More information and alternatives are available in the installation_ section of the documentation page.

Usage
-----

When EDDL is installed basic and advanced examples are compiled and build. Therefore, the user can practice with these exameples in order to get experience with the library and how can be used. On the documentation_ page video tutorials are provided aswell.


.. _installation: https://deephealthproject.github.io/eddl/intro/installation.html

.. _github: https://github.com/deephealthproject/eddl

.. _documentation: https://deephealthproject.github.io/eddl/index.html
