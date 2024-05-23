from atm_management.generic_view_mixins.custom_api_view import CustomAPIView
from rest_framework.response import Response

class APIRoot(CustomAPIView):

    def get(self, request):
        base_url = request.build_absolute_uri('/')
        return Response({
            "urls":  [
                base_url+"sites/state/upload/",
                base_url+"sites/state/",
                base_url+"sites/city/upload/",
                base_url+"sites/city/",
                base_url+"sites/",
                base_url+"sites/upload/",

            ]
        })