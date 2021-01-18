import requests
import json

def goal(apikey):
    url_all = 'https://wakatime.com/api/v1/users/current/all_time_since_today'
    