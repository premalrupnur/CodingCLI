import requests
import json

def dashboard(apikey):
    url_all = 'https://wakatime.com/api/v1/users/current/all_time_since_today'
    