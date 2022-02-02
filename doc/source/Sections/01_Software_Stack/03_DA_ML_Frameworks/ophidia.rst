Ophidia
=======

Ophidia is a CMCC Foundation research effort addressing Big Data challenges for eScience. The Ophidia framework represents an open source solution for the analysis of scientific multi-dimensional data, joining HPC paradigms and Big Data approaches. It provides an environment targeting High Performance Data Analytics (HPDA) through *parallel* and *in-memory data processing, data-driven task scheduling* and *server-side analysis*. The framework exploits an array-based storage model, leveraging the datacube abstraction from OLAP systems, and a hierarchical storage organisation to partition and distribute large multi-dimensional scientific datasets over multiple nodes. Ophidia is primarily used in the climate change domain, although it has also been successfully exploited in other scientific domains.

Ophidia official website: `https://ophidia.cmcc.it`.

Software license: GPLv3.

Installation
------------

The framework is composed by different software components. The source code for the various components is available on GitHub: `https://github.com/OphidiaBigData`. 

The installation guide is available at: `https://ophidia.cmcc.it/documentation/admin/index.html`.

For the client side, Ophidia also provides the Python bindings, called *PyOphidia*. To install PyOphidia:

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

The user guide documenting all the avaiable Ophidia features can be found at: `https://ophidia.cmcc.it/documentation/users/index.html`.
