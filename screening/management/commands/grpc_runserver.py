from django_grpc_framework.management.commands.grpcrunserver import Command as GrpcRunserverCommand


class Command(GrpcRunserverCommand):
    """Command to start a gRPC server."""

    help = "Starts a gRPC server."
    requires_system_checks = []
