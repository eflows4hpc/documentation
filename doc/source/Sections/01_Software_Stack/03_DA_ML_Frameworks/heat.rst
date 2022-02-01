HeAT
====


HeAT is a flexible and seamless open-source software for high performance data analytics and machine learning. 
It provides highly optimized algorithms and data structures for tensor computations using CPUs, GPUs and distributed 
cluster systems on top of MPI. The goal of Heat is to fill the gap between data analytics and machine learning 
libraries with a strong focus on single-node performance, and traditional high-performance computing (HPC). 
Heat's generic Python-first programming interface integrates seamlessly with the existing data science ecosystem 
and makes it as effortless as using numpy to write scalable scientific and data science applications.

HeAT allows you to tackle your actual Big Data challenges that go beyond the computational and memory needs of your laptop and desktop.


Installation 
------------

The simplest way of installing HeAT is to use pip:

::

   pip install heat[hdf5,netcdf]

More information can be found in project's git_ repository. 

Usage
-----

HeAT main features are:

* support for high-performance n-dimensional tensors

* efficient CPU, GPU and distributed computation using MPI

* powerful data analytics and machine learning methods

* abstracted communication via split tensors

* easy to grasp Python API


There are many usage examples in the git_ repository and documentation_. A good starting point for initial exploration is also 
the tutorial_. 



.. _git: https://github.com/helmholtz-analytics/heat/

.. _documentation: https://heat.readthedocs.io/en/latest/

.. _tutorial: https://github.com/helmholtz-analytics/heat/blob/master/scripts/tutorial.ipynb