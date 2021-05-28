from wardhacovidhelpapp.views import groceriesform
from django.contrib import admin
from django.contrib.admin.filters import ChoicesFieldListFilter
from .models import Groceries, PlasmaDonar, PlasmaRequest, TeamMembers, HospitalData,CovidNewsPost,VaccineAvailablity
# Register your models here.

from .forms import GroceriesFormView, PlasmaRequestFormView, PlasmaDonarFormView

class PlasmaRequestAdmin(admin.ModelAdmin):
    list_display = ["Name", "Age", "Gender", "BloodGroup",
                    "DateOfPositive", "verified", "complete"]
    form = PlasmaRequestFormView
    search_fields = ["Name", "BloodGroup"]
    list_editable = ['verified', 'complete']
    list_filter = ["BloodGroup"]


class PlasmaDonateAdmin(admin.ModelAdmin):
    list_display = ["Name", "Age", "Gender", "BloodGroup",
                    "DateOfNegative", "DateCreated", "verified"]
    form = PlasmaDonarFormView
    search_fields = ["Name", "BloodGroup"]
    list_filter = ["BloodGroup"]
    list_editable = ['verified']


class HospitalDataAdmin(admin.ModelAdmin):
    list_display = ["HospitalName", "PhoneNumber", "Verified"]
    list_editable = ["Verified"]

class CovidNewsPostAdmin(admin.ModelAdmin):
    list_display = ["Title","Date_Created"]
    search_fields = ["Title"]

class TeamMembersAdmin(admin.ModelAdmin):
    list_display =["Name" ,"Profession","JoiningDate"]
    search_fields = ["Name"]

class VaccineAvailablityAdmin(admin.ModelAdmin):
    list_display = ["id","Name","AvailableCapacity","VaccineName","MinAgeLimit","BlockName","DistrictName","FeeType","LastUpdated"]

class GroceriesAdmin(admin.ModelAdmin):
    list_display = ["Store_Name", "Phone_Number","Delivery_Type","Admin_Verified"]
    form = GroceriesFormView
    search_fields = ["Store_Name"]
    list_editable = ['Admin_Verified']



admin.site.register(PlasmaDonar, PlasmaDonateAdmin)
admin.site.register(PlasmaRequest, PlasmaRequestAdmin)
# admin.site.register(TeamMembers,TeamMembersAdmin)
admin.site.register(HospitalData, HospitalDataAdmin)
admin.site.register(CovidNewsPost,CovidNewsPostAdmin)
admin.site.register(VaccineAvailablity,VaccineAvailablityAdmin)
admin.site.register(Groceries,GroceriesAdmin)