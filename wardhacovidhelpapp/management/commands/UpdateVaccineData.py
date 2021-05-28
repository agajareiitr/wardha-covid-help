from django.core.management.base import BaseCommand
from wardhacovidhelpapp.models import VaccineAvailablity
import requests
import datetime

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = VaccineAvailablity
    
    def handle(self,*args, **options):
        self.model_name.objects.all().delete()
        todaydate = datetime.date.today().strftime("%d-%m-%Y")
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=377&date="+todaydate
        brow_headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"}
        data = requests.get(url,headers=brow_headers).json()
        for i in data["sessions"]:
            name = i['name']
            available_capacity= i['available_capacity']
            vaccine = i['vaccine']
            min_age_limit = i['min_age_limit']
            block_name = i["block_name"]
            district_name = i["district_name"]
            fee_type = i["fee_type"]
            data = self.model_name(Name=name,AvailableCapacity=available_capacity,VaccineName=vaccine,MinAgeLimit=min_age_limit,BlockName=block_name,DistrictName=district_name,FeeType=fee_type)
            data.save()