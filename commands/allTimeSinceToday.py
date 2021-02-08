import requests
import json
from halo import Halo
from termcolor import colored


def allTime(apikey):
    url_all = "https://wakatime.com/api/v1/users/current/all_time_since_today"
    spinner = Halo(text="Requesting Data", spinner="dots")
    spinner.start()
    try:
        response = requests.get(f"{url_all}?api_key={apikey}")
    except Exception as e:
        print(colored(e, "red"))
    data = response.json()
    print(data)
    spinner.stop()
    if response.status_code == 401:
        print(colored("Request Denied please enter correct API KEY", "red"))
    else:
        code_time = data["data"]["text"]
        if data["data"]["is_up_to_date"]:
            print(colored(f"CODING TIME SINCE WAKATIME LOGIN: {code_time}\n", "green"))
        else:
            print(colored("Your stats will be refreshed soon : Try it again .", "red"))
