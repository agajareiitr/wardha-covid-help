from django.db.models.expressions import OrderBy
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .forms import PlasmaDonarFormView, PlasmaRequestFormView,GroceriesFormView
from django.contrib import messages
from .listdata import VAICINE_PAGE_COWIN_INFO_MARATHI,VAICINE_PAGE_COWIN_INFO_ENGLISH

from .models import PlasmaDonar, PlasmaRequest, TeamMembers, HospitalData,CovidNewsPost,VaccineAvailablity,Groceries



def home_page(request):
    return render(request,"wardhacovidhelpapp/homepage.html")

def hospitalBed(request):
    return render(request,"wardhacovidhelpapp/hospitalBeds.html")

def vaccine_availablity(request):
    Centers = VaccineAvailablity.objects.all().order_by("-AvailableCapacity")
    content = {"Centers":Centers}
    return render(request,"wardhacovidhelpapp/vaccines_availablity.html",content)

def pharmacies(request):
    return render(request,"wardhacovidhelpapp/pharmacies.html")

def groceries(request):
    Stores = Groceries.objects.all().order_by("-Admin_Verified")
    content = {"Stores":Stores}
    return render(request,"wardhacovidhelpapp/groceries.html",content)

def meal_services(request):
    return render(request,"wardhacovidhelpapp/meal_services.html")

def covid_news(request):
    newsfront = CovidNewsPost.objects.values("id","Title","Short_Discription","News_Image","Date_Created").order_by("-Date_Created")
    
    content = {
        "Newsdata":newsfront
    }
    return render(request, "wardhacovidhelpapp/covid_news.html",content)

def detail_view_news(request,id):
    newsdata = CovidNewsPost.objects.get(id=id)
    content = {
        "newsdetails":newsdata
    }
    return render(request,"wardhacovidhelpapp/detailview.html",content)
def vaccinesdata(request):
    content = {
        "VAICINE_PAGE_COWIN_INFO_MARATHI":VAICINE_PAGE_COWIN_INFO_MARATHI,
        "VAICINE_PAGE_COWIN_INFO_ENGLISH":VAICINE_PAGE_COWIN_INFO_ENGLISH
    }
    return render(request, "wardhacovidhelpapp/vaccines.html",content)


def teamMembers(request):
    teammembers = TeamMembers.objects.all().order_by("JoiningDate")
    content = {"teammembers": teammembers}
    return render(request, "wardhacovidhelpapp/Teammembers.html", content)


def covidtestinglabs(request):
    Hospital_details1 = HospitalData.objects.all().order_by("-Verified","-id")
    Hospital_details = {"Hospital_details": Hospital_details1}
    
    return render(request, "wardhacovidhelpapp/CovidTestingLabs.html", Hospital_details)


def plasma_Request_Donar_list_view(request):
    data1 = PlasmaDonar.objects.all()
    data2 = PlasmaRequest.objects.all()
    content = {"PlasmaDonar": data1, "PlasmaRequest": data2}
    return render(request, "wardhacovidhelpapp/plasmaR&Dlist.html", content)




# Below Functions and FORMS:
def plasmarequestform(request):
    content = {}
    plasma_request_form = PlasmaRequestFormView(
        request.POST or None, request.FILES or None)

    if plasma_request_form.is_valid():
        plasma_request_form.save()
        patient_name = request.POST["Name"]
        msg1 = f"{patient_name}, Your Request form is Submitted Successfully we will call you for verification, Once its Verified your Name will show in the PLASMA REQUEST SECTION"
        msg2 = "आपला विनंती फॉर्म सबमिट केला गेला आहे, आम्ही आपल्याला Verification साठी कॉल करू, Verification झाल्यानंतर आपले नाव प्लाज्मा विनंती विभाग मध्ये दर्शविले जाईल धन्यवाद"
        messages.success(request, msg1)
        messages.success(request, msg2)
        return redirect('plasmarequestdonarlist_view_name')

    content['requestform'] = plasma_request_form
    return render(request, "wardhacovidhelpapp/RequestPlasmaform.html", content)


def plasmadonateform(request):
    content = {}
    plasma_donate_form = PlasmaDonarFormView(
        request.POST or None, request.FILES or None)

    if plasma_donate_form.is_valid():
        plasma_donate_form.save()
        Donar_name = request.POST["Name"]
        msg1 = f"{Donar_name}, Your Donation form is Submitted Successfully we will call you for verification, Once its Verified your Name will show in the PLASMA DONATE SECTION"
        msg2 = "आपला देणगी फॉर्म सबमिट केला गेला आहे, आम्ही आपल्याला Verification साठी कॉल करू, Verification झाल्यानंतर आपले नाव प्लाज्मा डोनार विभागात मध्ये दर्शविले जाईल धन्यवाद"
        messages.success(request, msg1)
        messages.success(request, msg2)
        return redirect('plasmarequestdonarlist_view_name')

    content['donateform'] = plasma_donate_form
    return render(request, "wardhacovidhelpapp/DonatePlasmaform.html", content)

def groceriesform(request):
    content = {}
    groceries_form = GroceriesFormView(request.POST or None, request.FILES or None)

    if groceries_form.is_valid():
        groceries_form.save()
        return redirect('home_page_name')
    
    content['groceriesform'] = groceries_form
    return render(request,"wardhacovidhelpapp/groceries_form.html",content)