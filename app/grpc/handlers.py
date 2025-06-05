from app.grpc import candidate_pb2_grpc
from app.grpc.services import CandidateStatusService


def grpc_handlers(server):
    """Register gRPC handlers.

    Args:
        server: gRPC server instance.
    """
    candidate_pb2_grpc.add_CandidateControllerServicer_to_server(CandidateStatusService.as_servicer(), server)
