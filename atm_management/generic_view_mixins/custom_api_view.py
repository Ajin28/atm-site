"""
This module consists of Base API view to be used for class based requests to review manager
"""
from rest_framework import status
from rest_framework.generics import GenericAPIView
from atm_management.exceptions.rest_api_exception import RestAPIException




class CustomAPIView(GenericAPIView):
    ''' A generic APIView for reviews project '''

    def validate_serializer(self, serializer, req_data):
        ''' Validate serializer against request data '''
        req = serializer(data=req_data)
        if not req.is_valid():
            raise RestAPIException(f"Please provide a valid request data", code=status.HTTP_400_BAD_REQUEST, errors=req.errors)
        return req.validated_data

    
    def validate_many_serializer(self, serializer, req_data, ):
        ''' Validate serializer against request data '''
        req = serializer(data=req_data, many=True)
        if not req.is_valid():
            raise RestAPIException(f"Please provide a valid request data", code=status.HTTP_400_BAD_REQUEST, errors=req.errors)
        return req.validated_data


