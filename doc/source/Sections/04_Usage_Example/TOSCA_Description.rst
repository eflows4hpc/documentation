Integration in TOSCA
====================

eFlows4HPC uses TOSCA to describe the high-level execution lifecycle of a workflow, enabling the orchestration of tasks with diverse nature.
For the Pillar I use case, TOSCA is used to coordinate the creation of a container image, its transfer to a target cluster,
stage-in of input data, PyCOMPSs computation, and stage-out the computation result to a data catalog.

An exhaustive list of TOSCA components developed in the context of the eFlows4HPC project and their configurable properties
can be found in section :ref:`section_hpcwaas_methodology_dev_ifce_tosca_comps`.

Section :ref:`section_usage_example_tosca_topology_template` describes how these components are assembled together in a
TOSCA topology template to implement the ROM Pillar I use case. More specifically you can refer to :numref:`tosca-topo-template`
to see how properties of the TOSCA components are used in this particular context.

.. _section_usage_example_tosca_topology_template:

ROM Pillar I topology template
------------------------------

The source code of this template is available in the
`workflow-registry github repository <https://github.com/eflows4hpc/workflow-registry/tree/main/rom_pillar_I/tosca>`_ in the eFlows4HPC organization.

This topology template composes the different components described above into
a TOSCA application that allows to implement the ROM Pillar I workflow.

The ROM Pillar I workflow is composed of two phases. First at deployment time the Image Creation Service is invoked to generate a container image
containing the required softwares, this image is then transferred to the target HPC cluster using the Data Logistic Service
(the ``DLSDAGImageTransfer`` TOSCA component). Once deployed the execution workflow can be invoked as many time as required.
This execution workflow consists in transferring input data from an HTTP server to the HPC cluster thanks to the DLS
(the ``HTTP2SSH`` TOSCA component), then run a PyCOMPSs job on those data (the ``PyCOMPSJob`` TOSCA component) and finally upload computation
results to an EUDAT repository using the DLS (the ``DLSDAGStageOutData`` TOSCA component).

:numref:`tosca-topo-template` shows how are defined the components and how they are connected together in order to run in sequence.
:numref:`fig_alien4cloud_minimal_workflow_topology` shows the same topology in a graphical way.

.. code-block:: yaml
    :name: tosca-topo-template
    :caption: Extract of the TOSCA topology template for ROM Pillar I workflow

    topology_template:
      inputs:
        debug:
          type: boolean
          required: true
          default: false
          description: "Do not redact sensible information on logs"
        user_id:
          type: string
          required: false
          default: ""
          description: "User id to use for authentication may be replaced with workflow input"
        vault_id:
          type: string
          required: false
          default: ""
          description: "User id to use for authentication may be replaced with workflow input"
        container_image_transfer_directory:
          type: string
          required: false
          description: "path of the image on the remote host"
        mid:
          type: string
          required: true
          description: "Uploaded Metadata ID"
        register_result_in_datacat:
          type: boolean
          required: false
          default: false
          description: "Should the record created in b2share be registered with data cat"
      node_templates:
        StageOutData:
          type: dls.ansible.nodes.DLSDAGStageOutData
          properties:
            mid: { get_input: mid }
            register: { get_input: register_result_in_datacat }
            input_name_for_mid: mid
            input_name_for_source_path: "result_data_path"
            input_name_for_register: register
            dls_api_username: { get_secret: [/secret/data/services_secrets/dls, data=username] }
            dls_api_password: { get_secret: [/secret/data/services_secrets/dls, data=password] }
            dag_id: "upload_example"
            debug: { get_input: debug }
            run_in_standard_mode: false
          requirements:
            - dependsOnAbstractEnvironmentExec_env:
                type_requirement: environment
                node: AbstractEnvironment
                capability: eflows4hpc.env.capabilities.ExecutionEnvironment
                relationship: tosca.relationships.DependsOn
            - dependsOnPyCompsJob2Feature:
                type_requirement: dependency
                node: PyCOMPSJob
                capability: tosca.capabilities.Node
                relationship: tosca.relationships.DependsOn
        ImageCreation:
          type: imagecreation.ansible.nodes.ImageCreation
          properties:
            service_url: "https://bscgrid20.bsc.es/image_creation"
            insecure_tls: true
            username: { get_secret: [/secret/data/services_secrets/image_creation, data=user] }
            password: { get_secret: [/secret/data/services_secrets/image_creation, data=password] }
            machine:
              container_engine: singularity
              platform: "linux/amd64"
              architecture: sandybridge
            workflow: "rom_pillar_I"
            step_id: "reduce_order_model"
            force: false
            debug: { get_input: debug }
            run_in_standard_mode: true
        DLSDAGImageTransfer:
          type: dls.ansible.nodes.DLSDAGImageTransfer
          properties:
            target_path: { get_input: container_image_transfer_directory }
            run_in_standard_mode: true
            dls_api_username: { get_secret: [/secret/data/services_secrets/dls, data=username] }
            dls_api_password: { get_secret: [/secret/data/services_secrets/dls, data=password] }
            dag_id: "transfer_image"
            debug: { get_input: debug }
            user_id: { get_input: user_id }
            vault_id: { get_input: vault_id }
          requirements:
            - dependsOnImageCreationFeature:
                type_requirement: dependency
                node: ImageCreation
                capability: tosca.capabilities.Node
                relationship: tosca.relationships.DependsOn
            - dependsOnAbstractEnvironmentExec_env:
                type_requirement: environment
                node: AbstractEnvironment
                capability: eflows4hpc.env.capabilities.ExecutionEnvironment
                relationship: tosca.relationships.DependsOn
        AbstractEnvironment:
          type: eflows4hpc.env.nodes.AbstractEnvironment
        PyCOMPSJob:
          type: org.eflows4hpc.pycompss.plugin.nodes.PyCOMPSJob
          properties:
            submission_params:
              qos: debug
              python_interpreter: python3
              num_nodes: 2
              extra_compss_opts: "--cpus_per_task --env_script=/reduce_order_model/env.sh"
            application:
              container_opts:
                container_opts: "-e"
                container_compss_path: "/opt/view/compss"
              arguments:
                - "$(dirname ${staged_in_file_path})"
                - "/reduce_order_model/ProjectParameters_tmpl.json"
                - "${result_data_path}/RomParameters.json"
              command: "/reduce_order_model/src/UpdatedWorkflow.py"
            keep_environment: true
          requirements:
            - dependsOnDlsdagImageTransferFeature:
                type_requirement: img_transfer
                node: DLSDAGImageTransfer
                capability: tosca.capabilities.Node
                relationship: tosca.relationships.DependsOn
            - dependsOnAbstractEnvironmentExec_env:
                type_requirement: environment
                node: AbstractEnvironment
                capability: eflows4hpc.env.capabilities.ExecutionEnvironment
                relationship: tosca.relationships.DependsOn
            - dependsOnHttp2SshFeature:
                type_requirement: dependency
                node: HTTP2SSH
                capability: tosca.capabilities.Node
                relationship: tosca.relationships.DependsOn
        HTTP2SSH:
          type: dls.ansible.nodes.HTTP2SSH
          properties:
            dag_id: plainhttp2ssh
            url: "https://b2drop.bsc.es/index.php/s/fQ85ZLDztG2t5j3/download/GidExampleSwaped.mdpa"
            force: true
            input_name_for_url: url
            input_name_for_target_path: "staged_in_file_path"
            dls_api_username: { get_secret: [/secret/data/services_secrets/dls, data=username] }
            dls_api_password: { get_secret: [/secret/data/services_secrets/dls, data=password] }
            debug: { get_input: debug }
            user_id: ""
            vault_id: ""
            run_in_standard_mode: false
          requirements:
            - dependsOnAbstractEnvironmentExec_env:
                type_requirement: environment
                node: AbstractEnvironment
                capability: eflows4hpc.env.capabilities.ExecutionEnvironment
                relationship: tosca.relationships.DependsOn
      workflows:
        exec_job:
          inputs:
            user_id:
              type: string
              required: true
            vault_id:
              type: string
              required: true
            result_data_path:
              type: string
              required: true
            staged_in_file_path:
              type: string
              required: true
            num_nodes:
              type: integer
              required: false
              default: 1
          steps:
            StageOutData_executing:
              target: StageOutData
              activities:
                - set_state: executing
              on_success:
                - StageOutData_run
            HTTP2SSH_submitted:
              target: HTTP2SSH
              activities:
                - set_state: submitted
              on_success:
                - HTTP2SSH_executing
            PyCOMPSJob_submitting:
              target: PyCOMPSJob
              activities:
                - set_state: submitting
              on_success:
                - PyCOMPSJob_submit
            PyCOMPSJob_submit:
              target: PyCOMPSJob
              operation_host: ORCHESTRATOR
              activities:
                - call_operation: tosca.interfaces.node.lifecycle.Runnable.submit
              on_success:
                - PyCOMPSJob_submitted
            StageOutData_submitted:
              target: StageOutData
              activities:
                - set_state: submitted
              on_success:
                - StageOutData_executing
            StageOutData_submitting:
              target: StageOutData
              activities:
                - set_state: submitting
              on_success:
                - StageOutData_submit
            StageOutData_run:
              target: StageOutData
              operation_host: ORCHESTRATOR
              activities:
                - call_operation: tosca.interfaces.node.lifecycle.Runnable.run
              on_success:
                - StageOutData_executed
            HTTP2SSH_executing:
              target: HTTP2SSH
              activities:
                - set_state: executing
              on_success:
                - HTTP2SSH_run
            PyCOMPSJob_submitted:
              target: PyCOMPSJob
              activities:
                - set_state: submitted
              on_success:
                - PyCOMPSJob_executing
            HTTP2SSH_submitting:
              target: HTTP2SSH
              activities:
                - set_state: submitting
              on_success:
                - HTTP2SSH_submit
            StageOutData_submit:
              target: StageOutData
              operation_host: ORCHESTRATOR
              activities:
                - call_operation: tosca.interfaces.node.lifecycle.Runnable.submit
              on_success:
                - StageOutData_submitted
            HTTP2SSH_run:
              target: HTTP2SSH
              operation_host: ORCHESTRATOR
              activities:
                - call_operation: tosca.interfaces.node.lifecycle.Runnable.run
              on_success:
                - HTTP2SSH_executed
            HTTP2SSH_executed:
              target: HTTP2SSH
              activities:
                - set_state: executed
              on_success:
                - PyCOMPSJob_submitting
            StageOutData_executed:
              target: StageOutData
              activities:
                - set_state: executed
            PyCOMPSJob_executing:
              target: PyCOMPSJob
              activities:
                - set_state: executing
              on_success:
                - PyCOMPSJob_run
            HTTP2SSH_submit:
              target: HTTP2SSH
              operation_host: ORCHESTRATOR
              activities:
                - call_operation: tosca.interfaces.node.lifecycle.Runnable.submit
              on_success:
                - HTTP2SSH_submitted
            PyCOMPSJob_executed:
              target: PyCOMPSJob
              activities:
                - set_state: executed
              on_success:
                - StageOutData_submitting
            PyCOMPSJob_run:
              target: PyCOMPSJob
              operation_host: ORCHESTRATOR
              activities:
                - call_operation: tosca.interfaces.node.lifecycle.Runnable.run
              on_success:
                - PyCOMPSJob_executed


.. _fig_alien4cloud_minimal_workflow_topology:

.. figure:: ../Figures/rom_pillar_I_tosca_topology.png
    :figwidth: 75 %
    :alt: Alien4Cloud ROM Pillar I topology
    :align: center

    Alien4Cloud ROM Pillar I topology
