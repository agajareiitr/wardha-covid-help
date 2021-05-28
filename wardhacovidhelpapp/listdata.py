
# HospitalsName = [
#     ["Mgims Sewagram","9881837950","MGIMS, Sevagram, Wardha MIDC, Wardha - 442003, Anna Sagar"],
#     ["Acharya VInoba Bhave Rural Hospital", "7152287702","Yavatmal Road, Wardha Ho, Wardha - 442001, Datta Meghe Institute Of Medical Sciences"],
#     [""]
# ]


# "आपला विनंती फॉर्म सबमिट केला गेला आहे, आम्ही आपल्याला Verification साठी कॉल करू, Verification झाल्यानंतर आपले नाव प्लाज्मा विनंती विभाग दर्शविले जाईल धन्यवाद"

# "आपला विनंती फॉर्म सबमिट केला गेला आहे, आम्ही आपल्याला Verification साठी कॉल करू, Verification झाल्यानंतर आपले नाव PLASMA REQUEST SECTION दर्शविले जाईल धन्यवाद"

# "आपला देणगी फॉर्म सबमिट केला आहे, आम्ही आपल्याला Verification साठी कॉल करू, Verification झाल्यानंतर आपले नाव प्लाज्मा डोनार विभागात मध्ये दर्शविले जाईल धन्यवाद"

import requests
# from bs4 import BeautifulSoup
# url = "https://www.diagnosticcentres.in/diagnostic-centres/maharashtra/wardha.html"

# data = requests.get(url)
# soup = BeautifulSoup(data.content,"html.parser")
# hosdetails =[]
# names = soup.find_all('a', class_="content_facility_btn btn btn-success",href=True)
# for i in range(len(names)):
#     url1 = names[i]['href']
#     if "thyrocare" in url1:
#         pass
#     else:
#         data1 = requests.get(url1)
#         soup1 = BeautifulSoup(data1.content,'html.parser')
#         name = soup1.find('div',class_="blog_details buisness-left")
#         name = name.getText().strip()
#         hosdetails.append(name)

# print(hosdetails)



# Hospital_list_raw = ['New Pete Blood Collecation\nAddress: Bhagat Singh Chowk, Ram Nagar, Wardha - 442001, Near Dr.dahase Hospital\nPhone: +91 7767010156, +91 9970788256', 'Anjali Pujari\nAddress: Anjali Lab, Main Road, Wardha - 442001, Near Lokvidyalay Bachelor Road\nPhone: +91 9823868796', 'Aarogya247365.com\nAddress: Wardha - 442001, Near Anand Homeopathic Clinic, Ingole Chowk,Malgujari Pura\nPhone: +91 8092247365\nWebsite: www.aarogya247365.com', 'Krishna Center For Clinical Reserch\nAddress: Seloo, Wardha - 442104, Bus Stop,Near Balaji Medical\nPhone: +91 7774992667', 'Dr. Makarande\nAddress: 21, Arvi Wardha Road, Wardha - 442001, Near Raj Automobiles Kelkarwadi\nPhone: +91 7152244785', 'Krupa Diagnostic Lab\nAddress: Arvi Road, Wardha - 442001\nPhone: +91 9850427976', 'Sahayog Pathology Lab\nAddress: Goras Bhandar Road Wardha, Ramnagar, Wardha - 442001\nPhone: +91 9850438433', 'Digno Lab\nAddress: Arvi Naka, Shiv Parvti Sbhagruh, Nr Dr Dahake Hospital, Wardha - 442001\nPhone: +91 9673447961', 'Vaishnavi Computerised Pathology Leboretary\nAddress: Near (Court)Kacheri, Ruparel Hotel, Hinganghat, Wardha, Hinganghat, WARDHA - 442301\nPhone: +91 9422143072, +91 7152247294', 'Sunita Wagh\nAddress: Jnmc Wardha, Main Road, Wardha - 442001, Near Bus Stand\nPhone: +91 9890625338', 'Amol Thakare\nAddress: Rashi Pathology Lab, Bachelor Road, Wardha - 442001, Near Bus Stand\nPhone: +91 9049755897', 'Rashi Pathology Lab\nAddress: Dhantoli Square, Bachlor Road, Wardha - 442001\nPhone: +91 7152251116', 'Rashi Diagnostic Centre\nAddress: 289, Gond Plot, Sudampuri, Wardha, Maharashtra 442001\nPhone: 07152 251 116', 'Magnum Life Sciences\nAddress: Arvi Road, Wardha - 442001, Arvi Naka\nPhone: +91 8390290420', 'New Fite Blood Collection Center\nAddress: Bhagatsingh Chowk, Ramnagar, Wardha - 442001, Ram Nagar\nPhone: +91 7767010156, +91 9970788256', 'Dr. Shyam Taori\nAddress: Indira Market Road, Inzhala, Wardha - 442306\nPhone: +91 9923446101, +91 7152242853', 'Metropolis Healthcare Ltd\nAddress: H No 306, Wanjari Chowk, Wardha, Maharashtra 442004\nPhone: 022 3399 3939', 'Khelkar Pathology\nAddress: Jagannath Ward, Hinganghat, WARDHA - 442301, Desh Seva Road\nPhone: +91 9890090445', 'Dr. Lal Pathlabs Ltd\nAddress: Turak Complex, Wardha - 442001, Borgaon Meghae\nPhone: +91 9049939298, 022 39885050\nWebsite: www.lalpathlabs.com']
# Hospital_list = [['New Pete Blood Collecation', 'Address: Bhagat Singh Chowk, Ram Nagar, Wardha - 442001, Near Dr.dahase Hospital', 'Phone: +91 7767010156, +91 9970788256'], ['Anjali Pujari', 'Address: Anjali Lab, Main Road, Wardha - 442001, Near Lokvidyalay Bachelor Road', 'Phone: +91 9823868796'], ['Aarogya247365.com', 'Address: Wardha - 442001, Near Anand Homeopathic Clinic, Ingole Chowk,Malgujari Pura', 'Phone: +91 8092247365', 'Website: www.aarogya247365.com'], ['Krishna Center For Clinical Reserch', 'Address: Seloo, Wardha - 442104, Bus Stop,Near Balaji Medical', 'Phone: +91 7774992667'], ['Dr. Makarande', 'Address: 21, Arvi Wardha Road, Wardha - 442001, Near Raj Automobiles Kelkarwadi', 'Phone: +91 7152244785'], ['Krupa Diagnostic Lab', 'Address: Arvi Road, Wardha - 442001', 'Phone: +91 9850427976'], ['Sahayog Pathology Lab', 'Address: Goras Bhandar Road Wardha, Ramnagar, Wardha - 442001', 'Phone: +91 9850438433'], ['Digno Lab', 'Address: Arvi Naka, Shiv Parvti Sbhagruh, Nr Dr Dahake Hospital, Wardha - 442001', 'Phone: +91 9673447961'], ['Vaishnavi Computerised Pathology Leboretary', 'Address: Near (Court)Kacheri, Ruparel Hotel, Hinganghat, Wardha, Hinganghat, WARDHA - 442301', 'Phone: +91 9422143072, +91 7152247294'], ['Sunita Wagh', 'Address: Jnmc Wardha, Main Road, Wardha - 442001, Near Bus Stand', 'Phone: +91 9890625338'], ['Amol Thakare', 'Address: Rashi Pathology Lab, Bachelor Road, Wardha - 442001, Near Bus Stand', 'Phone: +91 9049755897'], ['Rashi Pathology Lab', 'Address: Dhantoli Square, Bachlor Road, Wardha - 442001', 'Phone: +91 7152251116'], ['Rashi Diagnostic Centre', 'Address: 289, Gond Plot, Sudampuri, Wardha, Maharashtra 442001', 'Phone: 07152 251 116'], ['Magnum Life Sciences', 'Address: Arvi Road, Wardha - 442001, Arvi Naka', 'Phone: +91 8390290420'], ['New Fite Blood Collection Center', 'Address: Bhagatsingh Chowk, Ramnagar, Wardha - 442001, Ram Nagar', 'Phone: +91 7767010156, +91 9970788256'], ['Dr. Shyam Taori', 'Address: Indira Market Road, Inzhala, Wardha - 442306', 'Phone: +91 9923446101, +91 7152242853'], ['Metropolis Healthcare Ltd', 'Address: H No 306, Wanjari Chowk, Wardha, Maharashtra 442004', 'Phone: 022 3399 3939'], ['Khelkar Pathology', 'Address: Jagannath Ward, Hinganghat, WARDHA - 442301, Desh Seva Road', 'Phone: +91 9890090445'], ['Dr. Lal Pathlabs Ltd', 'Address: Turak Complex, Wardha - 442001, Borgaon Meghae', 'Phone: +91 9049939298, 022 39885050', 'Website: www.lalpathlabs.com']]
# Hospital_verify = [True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
# for i in Hospital_list_raw:
#     b = i.split("\n")
#     Hospital_list.append(b)
# b=1
# for i in Hospital_list:
#     Name = i[0]
#     address = i[1]
#     Phone = i[2] 
#     # data = HospitalData(HospitalName=Name,Address=address,PhoneNumber=Phone)
#     # data.save()
#     print(b,Name)
#     b +=1

# vaccine Availablity Script
# from wardhacovidhelpapp.models import VaccineAvailablity
# VaccineAvailablity.objects.all().delete()
# import requests
# url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=377&date=24-05-2021"
# brow_headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"}
# data = requests.get(url,headers=brow_headers).json()
# for i in data["sessions"]:
#     name = i['name']
#     available_capacity= i['available_capacity']
#     vaccine = i['vaccine']
#     min_age_limit = i['min_age_limit']
#     block_name = i["block_name"]
#     district_name = i["district_name"]
#     fee_type = i["fee_type"]
#     data = VaccineAvailablity(Name=name,AvailableCapacity=available_capacity,VaccineName=vaccine,MinAgeLimit=min_age_limit,BlockName=block_name,DistrictName=district_name,FeeType=fee_type)
#     data.save()


MAIN_PAGE_HELPLINE_PHONENUMBERS = [["Resident Deputy Collector", "07152-240872"],
     ["Superintendent collector office", "07152-243466"],
     ["Toll Free No.", "18002332383"],
     ["Women Helpline", "1091"],
     ["Child Helpline", "1098"],
     ["Police", "100"],
     ["Accident", "108"],
     ["Z.P. Wardha", "07152-240231"],
     ["NIC Helpdesk", "1800111555"]]

VAICINE_PAGE_COWIN_INFO_MARATHI = [
"१. सर्वात आधी https://selfregistration.cowin.gov.in/ वर जा. आपला मोबाइल नंबर टाका. त्यानंतर Get OTP वर क्लिक करा. ओटीपी मिळाल्यानंतर त्याला एन्टर करा. नंतर ‘Verify’ वर क्लिक करा.",
"२. यानंतर ‘Register for Vaccination’ पेजवर आपला फोटो आयडी प्रूफ, नाव, जेंडर आणि जन्मतारीख सोबत सर्व माहिती भरा.",
"३. असे केल्यानंतर तुम्हाला अपॉइंटमेट शेड्यूल करण्याचा ऑप्शन मिळेल. रजिस्ट्रेशन केल्यानंतर ‘Schedule’ बटनवर क्लिक करा.",
"४. यानंतर तुम्ही तुमचा पिनकोड टाका, सर्च वर क्लिक करा. या पिन कोड सोबत सेंटर दिसतील.",
"५. तुमच्या हिशोबाप्रमाणे सेंटर, डेट आणि टाइमची निवड करून ‘Confirm’वर क्लिक करा"]


VAICINE_PAGE_COWIN_INFO_ENGLISH =  [
"1. First go to https://selfregistration.cowin.gov.in/. Enter your mobile number. Then click on Get OTP. Enter it after receiving the OTP. Then click on ‘Verify’.",
"2. Then fill in all the information along with your photo ID proof, name, gender and date of birth on the ‘Register for Vaccination’ page.",
"3. After doing so, you will have the option to schedule an appointment. After registration click on Schedule button.",
"4. After that you enter your pincode, click on search. Centers will appear along with this pin code.",
"5. Select the center, date and time as per your account and click on ‘Confirm’"
]

