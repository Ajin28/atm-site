from atm_management.generic_view_mixins.custom_api_view import CustomAPIView
from atm_management.model_queries import ATMCityModelQueries
from rest_framework.response import Response

class CityListView(CustomAPIView, ATMCityModelQueries):

    def get(self, request):

        return Response({
            "status": 1,
            "result": self.format_response_data(self.get_all_city())
        }) 

    def format_response_data(self, queryset):
        data_list = list()
        for city_obj in queryset:
            data_list.append({
                "id": city_obj.id,
                "name": city_obj.name.title(),
                "state": city_obj.state.name.title(),
                "abb":  city_obj.state.abbreviation
            })

        return data_list



