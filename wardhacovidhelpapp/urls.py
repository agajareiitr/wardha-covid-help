from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_page,name="home_page_name"),
    path("Plasma-Request-form",views.plasmarequestform,name="plasmarequestformview_name"),
    path("Plasma-Donate-form",views.plasmadonateform,name="plasmadonateformview_name"),
    path("Plasma-requests-and-donars",views.plasma_Request_Donar_list_view,name="plasmarequestdonarlist_view_name"),
    path("covid-testing-labs",views.covidtestinglabs,name="covidtestinglabs_name"),
    path("team-members",views.teamMembers,name="teammembers_name"),
    path("vaccines",views.vaccinesdata,name="vaccinesdata_name"),
    path("covid-news",views.covid_news,name = "covid_news_name"),
    path("News/<int:id>/",views.detail_view_news,name='detailview_name'),
    path("HospitalBed",views.hospitalBed,name="hospital_beds_name"),
    path("vaccine-availablity",views.vaccine_availablity,name="vaccines_availablity_name"),
    path("pharmacies",views.pharmacies,name="pharmacies_name"),
    path("groceries",views.groceries,name="groceries_name"),
    path("groceries-form",views.groceriesform,name="groceries_form_name"),
    path("meal-servies",views.meal_services,name="meal_services_name"),


]