from atm_management.generic_view_mixins.custom_api_view import CustomAPIView
from atm_management.model_queries import ATMSiteModelQueries
from rest_framework.response import Response

class SiteListView(CustomAPIView, ATMSiteModelQueries):

    def get(self, request):

        return Response({
            "status": 1,
            "result": self.format_response_data(self.get_all_sites())
        }) 

    def format_response_data(self, atm_queryset):
        data_list = list()
        for atm_obj in atm_queryset:
            data_list.append({
                "site_id": atm_obj.site_id,
                "name": atm_obj.name,
                "phone_number": atm_obj.contact_details["phone_number"] if atm_obj.contact_details and "phone_number" in atm_obj.contact_details else None,
                "email": atm_obj.contact_details["email"] if atm_obj.contact_details and "email" in atm_obj.contact_details else None,
                "pincode": atm_obj.pincode,
                "address_line_1": atm_obj.address_line_1,
                "address_line_2": atm_obj.address_line_2,
                "city": atm_obj.city.name.title(),
                "state": atm_obj.city.state.name.title(),
                "state_abb":  atm_obj.city.state.abbreviation,
            })

        return data_list



