from atm_management.generic_view_mixins.custom_api_view import CustomAPIView
from atm_management.model_queries import ATMStateModelQueries
from rest_framework.response import Response

class StateListView(CustomAPIView, ATMStateModelQueries):

    def get(self, request):

        return Response({
            "status": 1,
            "result": self.format_response_data(self.get_all_state())
        }) 

    def format_response_data(self, queryset):
        data_list = list()
        for state_obj in queryset:
            data_list.append({
                "id": state_obj.id,
                "name": state_obj.name.title(),
                "abb": state_obj.abbreviation
            })

        return data_list



