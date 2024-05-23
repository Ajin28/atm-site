from django.urls import path
from atm_management.views import *


urlpatterns = [
    path('', SiteListView.as_view()),  
    path('upload/', UploadSiteView.as_view()),  

    path('state/', StateListView.as_view()),  
    path('state/upload/', UploadStateView.as_view()),

    path('city/', CityListView.as_view()),  
    path('city/upload/', UploadCityView.as_view()) 

]
