# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import EnlaceRn_pb2 as EnlaceRn__pb2


class EnlaceRnStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.autentificacion = channel.unary_unary(
                '/enlacern.EnlaceRn/autentificacion',
                request_serializer=EnlaceRn__pb2.usuarioRequest.SerializeToString,
                response_deserializer=EnlaceRn__pb2.usuarioResponse.FromString,
                )
        self.registrarEnlace = channel.unary_unary(
                '/enlacern.EnlaceRn/registrarEnlace',
                request_serializer=EnlaceRn__pb2.EnlaceRequest.SerializeToString,
                response_deserializer=EnlaceRn__pb2.EnlaceResponse.FromString,
                )
        self.getEnlace = channel.unary_unary(
                '/enlacern.EnlaceRn/getEnlace',
                request_serializer=EnlaceRn__pb2.clientesRequest.SerializeToString,
                response_deserializer=EnlaceRn__pb2.EnlaceResponse.FromString,
                )
        self.getEnlaces = channel.unary_unary(
                '/enlacern.EnlaceRn/getEnlaces',
                request_serializer=EnlaceRn__pb2.enlace.SerializeToString,
                response_deserializer=EnlaceRn__pb2.ListaEnlace.FromString,
                )
        self.getClientes = channel.unary_unary(
                '/enlacern.EnlaceRn/getClientes',
                request_serializer=EnlaceRn__pb2.clientesRequest.SerializeToString,
                response_deserializer=EnlaceRn__pb2.clienteReponse.FromString,
                )


class EnlaceRnServicer(object):
    """Missing associated documentation comment in .proto file."""

    def autentificacion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def registrarEnlace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getEnlace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getEnlaces(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getClientes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EnlaceRnServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'autentificacion': grpc.unary_unary_rpc_method_handler(
                    servicer.autentificacion,
                    request_deserializer=EnlaceRn__pb2.usuarioRequest.FromString,
                    response_serializer=EnlaceRn__pb2.usuarioResponse.SerializeToString,
            ),
            'registrarEnlace': grpc.unary_unary_rpc_method_handler(
                    servicer.registrarEnlace,
                    request_deserializer=EnlaceRn__pb2.EnlaceRequest.FromString,
                    response_serializer=EnlaceRn__pb2.EnlaceResponse.SerializeToString,
            ),
            'getEnlace': grpc.unary_unary_rpc_method_handler(
                    servicer.getEnlace,
                    request_deserializer=EnlaceRn__pb2.clientesRequest.FromString,
                    response_serializer=EnlaceRn__pb2.EnlaceResponse.SerializeToString,
            ),
            'getEnlaces': grpc.unary_unary_rpc_method_handler(
                    servicer.getEnlaces,
                    request_deserializer=EnlaceRn__pb2.enlace.FromString,
                    response_serializer=EnlaceRn__pb2.ListaEnlace.SerializeToString,
            ),
            'getClientes': grpc.unary_unary_rpc_method_handler(
                    servicer.getClientes,
                    request_deserializer=EnlaceRn__pb2.clientesRequest.FromString,
                    response_serializer=EnlaceRn__pb2.clienteReponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'enlacern.EnlaceRn', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EnlaceRn(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def autentificacion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/enlacern.EnlaceRn/autentificacion',
            EnlaceRn__pb2.usuarioRequest.SerializeToString,
            EnlaceRn__pb2.usuarioResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def registrarEnlace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/enlacern.EnlaceRn/registrarEnlace',
            EnlaceRn__pb2.EnlaceRequest.SerializeToString,
            EnlaceRn__pb2.EnlaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getEnlace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/enlacern.EnlaceRn/getEnlace',
            EnlaceRn__pb2.clientesRequest.SerializeToString,
            EnlaceRn__pb2.EnlaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getEnlaces(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/enlacern.EnlaceRn/getEnlaces',
            EnlaceRn__pb2.enlace.SerializeToString,
            EnlaceRn__pb2.ListaEnlace.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getClientes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/enlacern.EnlaceRn/getClientes',
            EnlaceRn__pb2.clientesRequest.SerializeToString,
            EnlaceRn__pb2.clienteReponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
