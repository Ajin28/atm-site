from atm_management.models import ATMCity
from atm_management.model_queries import ATMStateModelQueries

class ATMCityModelQueries:

    def get_all_city(self):
        return ATMCity.objects.all()
    
    def get_or_create_city(self, city, state):
        created = False
        city_name = city.lower()
        try:
            city = ATMCity.objects.get(name=city_name)
        except ATMCity.DoesNotExist:
            city = ATMCity.objects.create(name=city_name, state_id=state)
            created = True
            city.save()
        return created, city
  
    def update_or_create_city(self, city, state):
        created = False
        city_name = city.lower()
        _, state_obj = ATMStateModelQueries().get_or_create_state(state)
        try:
            city_obj = ATMCity.objects.get(name=city_name)
            city_obj.state_id = state_obj.id
        except ATMCity.DoesNotExist:
            city_obj = ATMCity.objects.create(name=city_name, state_id = state_obj.id)
            created = True
        
        city_obj.save()
        return created, city_obj