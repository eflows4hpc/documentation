Alien4Cloud
===========

Alien4Cloud is an REST API and a Graphical User Interface that allows to store, design and deploy complex
applications made of reusable components thanks to the TOSCA_ specification.

In the context of eflows4hpc, Alien4Cloud will be used by a workflow developer to design and deploy applicative workflows.
End users will not interact directly with Alien4Cloud but with a simplified REST interface called the HPC workflow as a Service (WaaS) API.
The WaaS API will in turn interact with Alien4Cloud REST API to execute the workflows.

Alien4Cloud relies on the Yorc orchestration engine to actually execute the workflows.

Alien4Cloud is an open source project developed by Atos. The source code can be found in project repository_ and the documentation_
is available online.


.. _TOSCA: https://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.3/TOSCA-Simple-Profile-YAML-v1.3.html
.. _repository: https://github.com/eflows4hpc/alien4cloud
.. _documentation: https://alien4cloud.github.io/#/documentation/3.3.0/index.html
