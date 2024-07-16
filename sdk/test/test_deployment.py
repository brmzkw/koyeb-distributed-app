# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.deployment import Deployment

class TestDeployment(unittest.TestCase):
    """Deployment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Deployment:
        """Test Deployment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Deployment`
        """
        model = Deployment()
        if include_optional:
            return Deployment(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                allocated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                succeeded_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                terminated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                organization_id = '',
                app_id = '',
                service_id = '',
                parent_id = '',
                child_id = '',
                status = 'PENDING',
                metadata = openapi_client.models.deployment_metadata.DeploymentMetadata(
                    trigger = openapi_client.models.trigger_deployment_metadata.TriggerDeploymentMetadata(
                        type = 'UNKNOWN_TYPE', 
                        actor = 'UNKNOWN_ACTOR', 
                        git = openapi_client.models.trigger_git_deployment_metadata.TriggerGitDeploymentMetadata(
                            provider = 'UNKNOWN', 
                            repository = '', 
                            branch = '', 
                            sha = '', 
                            message = '', 
                            sender_username = '', 
                            sender_avatar_url = '', 
                            sender_profile_url = '', ), ), 
                    database = openapi_client.models.database_deployment_metadata.DatabaseDeploymentMetadata(
                        neon_postgres = openapi_client.models.neon_postgres_database_deployment_metadata.NeonPostgresDatabaseDeploymentMetadata(
                            reset_role_passwords = [
                                ''
                                ], ), ), 
                    git = openapi_client.models.git_deployment_metadata.GitDeploymentMetadata(
                        last_provisioned_deployment_id = '', ), 
                    archive = openapi_client.models.archive_deployment_metadata.ArchiveDeploymentMetadata(
                        last_provisioned_deployment_id = '', ), ),
                definition = openapi_client.models.deployment_definition.DeploymentDefinition(
                    name = '', 
                    type = 'INVALID', 
                    routes = [
                        openapi_client.models.deployment_route.DeploymentRoute(
                            port = 56, 
                            path = '', )
                        ], 
                    ports = [
                        openapi_client.models.deployment_port.DeploymentPort(
                            port = 56, 
                            protocol = '', )
                        ], 
                    env = [
                        openapi_client.models.deployment_env.DeploymentEnv(
                            scopes = [
                                ''
                                ], 
                            key = '', 
                            value = '', 
                            secret = '', )
                        ], 
                    regions = [
                        ''
                        ], 
                    scalings = [
                        openapi_client.models.deployment_scaling.DeploymentScaling(
                            min = 56, 
                            max = 56, 
                            targets = [
                                openapi_client.models.deployment_scaling_target.DeploymentScalingTarget(
                                    average_cpu = openapi_client.models.deployment_scaling_target_average_cpu.DeploymentScalingTargetAverageCPU(
                                        value = 56, ), 
                                    average_mem = openapi_client.models.deployment_scaling_target_average_mem.DeploymentScalingTargetAverageMem(
                                        value = 56, ), 
                                    requests_per_second = openapi_client.models.deployment_scaling_target_requests_per_second.DeploymentScalingTargetRequestsPerSecond(
                                        value = 56, ), 
                                    concurrent_requests = openapi_client.models.deployment_scaling_target_concurrent_requests.DeploymentScalingTargetConcurrentRequests(
                                        value = 56, ), 
                                    requests_response_time = openapi_client.models.deployment_scaling_target_requests_response_time.DeploymentScalingTargetRequestsResponseTime(
                                        value = 56, 
                                        quantile = 56, ), )
                                ], )
                        ], 
                    instance_types = [
                        openapi_client.models.deployment_instance_type.DeploymentInstanceType()
                        ], 
                    health_checks = [
                        openapi_client.models.deployment_health_check.DeploymentHealthCheck(
                            grace_period = 56, 
                            interval = 56, 
                            restart_limit = 56, 
                            timeout = 56, 
                            tcp = openapi_client.models.tcp_health_check.TCPHealthCheck(
                                port = 56, ), 
                            http = openapi_client.models.http_health_check.HTTPHealthCheck(
                                port = 56, 
                                path = '', 
                                method = '', 
                                headers = [
                                    openapi_client.models.http_header.HTTPHeader(
                                        key = '', 
                                        value = '', )
                                    ], ), )
                        ], 
                    volumes = [
                        openapi_client.models.deployment_volume.DeploymentVolume(
                            id = '', 
                            path = '', 
                            replica_index = 56, )
                        ], 
                    skip_cache = True, 
                    docker = openapi_client.models.docker_source.DockerSource(
                        image = '', 
                        command = '', 
                        args = [
                            ''
                            ], 
                        image_registry_secret = '', 
                        entrypoint = [
                            ''
                            ], 
                        privileged = True, ), 
                    git = openapi_client.models.git_source.GitSource(
                        repository = '', 
                        branch = '', 
                        tag = '', 
                        sha = '', 
                        build_command = '', 
                        run_command = '', 
                        no_deploy_on_push = True, 
                        workdir = '', 
                        buildpack = openapi_client.models.buildpack_builder.BuildpackBuilder(
                            build_command = '', 
                            run_command = '', 
                            privileged = True, ), ), 
                    database = openapi_client.models.database_source.DatabaseSource(
                        neon_postgres = openapi_client.models.neon_postgres_database.NeonPostgresDatabase(
                            pg_version = 56, 
                            region = '', 
                            instance_type = '', 
                            roles = [
                                openapi_client.models.neon_postgres_database/neon_role.NeonPostgresDatabase.NeonRole(
                                    name = '', 
                                    secret = '', )
                                ], 
                            databases = [
                                openapi_client.models.neon_postgres_database/neon_database.NeonPostgresDatabase.NeonDatabase(
                                    name = '', 
                                    owner = '', )
                                ], ), ), 
                    archive = openapi_client.models.archive_source.ArchiveSource(
                        id = '', ), ),
                messages = [
                    ''
                    ],
                provisioning_info = openapi_client.models.deployment_provisioning_info.DeploymentProvisioningInfo(
                    sha = '', 
                    image = '', 
                    stages = [
                        openapi_client.models.deployment_provisioning_info/stage.DeploymentProvisioningInfo.Stage(
                            name = '', 
                            status = 'UNKNOWN', 
                            messages = [
                                ''
                                ], 
                            started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            build_attempts = [
                                openapi_client.models.deployment_provisioning_info/stage/build_attempt.DeploymentProvisioningInfo.Stage.BuildAttempt(
                                    id = 56, 
                                    started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], )
                        ], ),
                database_info = openapi_client.models.deployment_database_info.DeploymentDatabaseInfo(
                    neon_postgres = openapi_client.models.deployment_neon_postgres_database_info.DeploymentNeonPostgresDatabaseInfo(
                        active_time_seconds = '', 
                        compute_time_seconds = '', 
                        written_data_bytes = '', 
                        data_transfer_bytes = '', 
                        data_storage_bytes_hour = '', 
                        server_host = '', 
                        server_port = 56, 
                        endpoint_state = '', 
                        endpoint_last_active = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        default_branch_id = '', 
                        default_branch_name = '', 
                        default_branch_state = '', 
                        default_branch_logical_size = '', 
                        roles = [
                            openapi_client.models.deployment_neon_postgres_database_info_role.DeploymentNeonPostgresDatabaseInfoRole(
                                name = '', 
                                secret_id = '', )
                            ], ), ),
                skip_build = True,
                role = 'INVALID',
                version = '',
                deployment_group = ''
            )
        else:
            return Deployment(
        )
        """

    def testDeployment(self):
        """Test Deployment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
