from atm_management.models import ATMState

class ATMStateModelQueries:

    def get_all_state(self):
        return ATMState.objects.all()
    
    
    def get_or_create_state(self, state, abb=None):
        created = False
        state_name = state.lower()
        try:
            state = ATMState.objects.get(name=state_name)
        except ATMState.DoesNotExist:
            state = ATMState.objects.create(name=state_name, abbreviation=None)
            state.save()
            created = True
        return created, state
    
      
    def update_or_create_state(self, state, abb=None):
        created = False
        state_name = state.lower()
        try:
            state = ATMState.objects.get(name=state_name)
        except ATMState.DoesNotExist:
            state = ATMState.objects.create(name=state_name)
            created = True
 
        state.abbreviation = abb
        state.save()
        return created, state

  