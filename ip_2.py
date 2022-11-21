from requests import get

loc = get('https://ipapi.co/json/')
print(loc.json())
