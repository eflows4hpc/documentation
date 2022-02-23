Ophidia
=======

`Ophidia <https://ophidia.cmcc.it>`_ is a `CMCC Foundation <https://www.cmcc.it/>`_ research effort addressing Big Data challenges for eScience. The Ophidia framework represents an open source solution for the analysis of scientific multi-dimensional data, joining HPC paradigms and Big Data approaches. It provides an environment targeting High Performance Data Analytics (HPDA) through *parallel* and *in-memory data processing, data-driven task scheduling* and *server-side analysis*. The framework exploits an array-based storage model, leveraging the datacube abstraction from OLAP systems, and a hierarchical storage organisation to partition and distribute large multi-dimensional scientific datasets over multiple nodes. Ophidia is primarily used in the climate change domain, although it has also been successfully exploited in other scientific domains.

Software license: GPLv3.

Installation
------------

The framework is composed by different software components. The source code for the various components is available on `GitHub <https://github.com/OphidiaBigData>`_. 

The installation guide is available in the `documentation <https://ophidia.cmcc.it/documentation/admin/index.html>`_.

For the client side, Ophidia also provides the Python bindings, called `PyOphidia <https://pypi.org/project/PyOphidia/>`_. To install PyOphidia:

::

    pip install pyophidia
  
or to install in a *Conda* environment:

::

    conda install -c conda-forge pyophidia

Usage
-----

Ophidia provides features for data management and analysis, such as:

- data reduction and subsetting
- data intercomparison
- array processing
- time series analysis
- statistical and mathematical operations
- data manipulation and transformation
- interactive data exploration

The `user guide <https://ophidia.cmcc.it/documentation/users/index.html>`_ documents all the available Ophidia features.
