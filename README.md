# wardha-covid-help

# Explore the Website:
1. Go to [https://www.wardhacovidhelp.online/](https://www.wardhacovidhelp.online/) to see the actual Website
2. Now go to admin panel [https://www.wardhacovidhelp.online/admin](https://www.wardhacovidhelp.online/admin) to see how data is managed in Backend.
3. for Credentials use :
    1. Username : ```demo```
    2. Password : ```pass@1234```
4. Use the Above Credetials to log in. (! above credentials have only view Permissions )


# Steps to Download and run this Website :

1. Download this repository using ``` git clone https://github.com/agajareiitr/wardha-covid-help.git``` in some folder
2. Make a Virtual Environment using ```python -m venv yourenvname```.
3. activate your ```yourvenvname``` using  ``` yourvenvname\Scripts\activate``` or ``` yourvenvname\Scripts\activate.bat``` command in command line.
4. Now go to ```wardhacovidhelp``` directory and run followings command :
    1. `pip install -r requirements.txt`
    2. ```python manage.py makemigrations```
    3. ```python manage.py migrate```
    4. ```python manage.py createsuperuser```
5. Now run ``` python manage.py runserver```
6. Now go to ```127.0.0.1:8000``` to see the website.
----

# Website Demo Images :

## Main Page :
![Screenshot (129)](https://user-images.githubusercontent.com/39427280/119941545-608cff80-bfae-11eb-9671-19fb9ed48b54.png)

## Grocerry Store :
![Screenshot (130)](https://user-images.githubusercontent.com/39427280/119941609-74d0fc80-bfae-11eb-9cad-07b3d46d77e4.png)

## How to register for Vaccine :
![Screenshot (131)](https://user-images.githubusercontent.com/39427280/119941655-874b3600-bfae-11eb-8086-9f534be88d37.png)

## Covid-19 Vaccine Centers and the Availablity of Vaccine, this data is updates Everyday :
![Screenshot (132)](https://user-images.githubusercontent.com/39427280/119941775-a8ac2200-bfae-11eb-9700-c4cb13de8a74.png)

## Covid-19 Testing Labs Info :
![Screenshot (133)](https://user-images.githubusercontent.com/39427280/119941823-b95c9800-bfae-11eb-885a-7d62754b99f7.png)

## News Page (This Page contains only Covid News ) :
![Screenshot (134)](https://user-images.githubusercontent.com/39427280/119941882-cb3e3b00-bfae-11eb-8831-9b09618d0edd.png)
