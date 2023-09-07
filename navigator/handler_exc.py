from rest_framework import status
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    return Response({}, status=status.HTTP_400_BAD_REQUEST)


def errors_handler(*args, **kwargs):
    return Response({}, status=status.HTTP_400_BAD_REQUEST)
