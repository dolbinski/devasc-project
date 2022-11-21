# devasc-project

#1. First Option
#You can install this library using the pip command like this:
$ pip install requests
#As we discussed, we'll first fetch our IP address from the first API. Then we'll make use of this IP address to fetch location information for this particular IP address. So, we'll have two functions:
import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


print(get_location())

#2.Second option
pip install requests


from requests import get

loc = get('https://ipapi.co/json/')
print(loc.json())
