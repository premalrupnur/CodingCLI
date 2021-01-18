import requests
import json

def dashboard(apikey):
    url_dashboard = 'https://wakatime.com/api/v1/users/current/dashboard'
    response = requests.get(f'{url_dashboard}?api_key={apikey}')
    rawdata = response.json
    print(rawdata)
    