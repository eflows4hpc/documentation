Development Interface
=====================

Setup
-----

Alien4Cloud & Yorc
##################

Please refer to the documentation of the Alien4Cloud & Yorc project for more information.

A instance of Alien4Cloud and Yorc is available on Juelich cloud, ask to the project to have an access

Importing required components into Alien4Cloud
##############################################

Some TOSCA components and topologies templates need to be imported into Alien4Cloud.
If you are using the instance on Juelich cloud, this is already done and you can move to the next paragraph.

You should first move to the ``Catalog`` tab and then the ``Manage archives`` tab, finally click on ``Git import`` to add components.

.. figure:: Figures/catalog.png
    :figwidth: 50 %
    :alt: Alien4Cloud catalog
    :align: center

    Click on ``Git import`` to add components

You should have at least the three repositories defined as shown in :numref:`fig_alien4cloud_git_catalog`:

.. _fig_alien4cloud_git_catalog:
.. figure:: Figures/git-catalog.png
    :figwidth: 50 %
    :alt: Alien4Cloud git catalog
    :align: center

    Click on ``Git location`` to define imports from a git repository


Click on ``Git location`` to define imports from a git repository as shown in :numref:`fig_alien4cloud_git_import_setup`

.. _fig_alien4cloud_git_import_setup:
.. figure:: Figures/git-import-setup.png
    :figwidth: 50 %
    :alt: Alien4Cloud setup a catalog git repository
    :align: center

    Alien4Cloud setup a catalog git repository

Once done you can click on ``Import all``.

Creating an application based on the minimal workflow example
-------------------------------------------------------------

Move to the ``Applications`` tab and click on ``New application``.

.. figure:: Figures/applications.png
    :figwidth: 50 %
    :alt: Alien4Cloud applications list
    :align: center

    Manage applications in Alien4Cloud

Then create a new application based on the minimal workflow template as shown in :numref:`fig_alien4cloud_app_create`

.. _fig_alien4cloud_app_create:
.. figure:: Figures/new-application.png
    :figwidth: 50 %
    :alt: Alien4Cloud create a new application
    :align: center

    Alien4Cloud create a template based application

Edit the topology to fit your needs:

.. figure:: Figures/topology.png
    :figwidth: 50 %
    :alt: Alien4Cloud minimal workflow topology
    :align: center

    Alien4Cloud minimal workflow topology

Then click on ``Deploy`` to deploy the application.

.. figure:: Figures/deploy.png
    :figwidth: 50 %
    :alt: Alien4Cloud deploy an application
    :align: center

    Alien4Cloud deploy an application

Make your workflow available to end-users using the WaaS API
------------------------------------------------------------

In order for the WaaS API to know which workflow to allow users to use, you should add a specific tag to your Alien4Cloud application.
Move to your application main panel and under the ``Tags`` section add a tag named ``hpcwaas-workflows``.
The tag value should be a coma-separated list of workflow names that could be called through the HPC WaaS API.
In the minimal workflow example, this tag value should be ``exec_job``.
