from atm_management.models import ATMSite

class ATMSiteModelQueries:

    def get_all_sites(self):
        return ATMSite.objects.all().select_related('city', 'city__state')
    
    def get_or_create_atm_site(self, site_id):
        created = False
        try:
            atm_obj = ATMSite.objects.get(site_id=site_id)
        except ATMSite.DoesNotExist:
            atm_obj = ATMSite(site_id=site_id)
            created = True
        return created, atm_obj

  