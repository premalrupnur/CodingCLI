import requests
import json
from halo import Halo
from tabulate import tabulate
from termcolor import colored


def language(apikey: str):
    url_all = "https://wakatime.com/api/v1/users/current/stats/last_7_days"
    spinner = Halo(text="Requesting Data", spinner="dots")
    spinner.start()
    try:
        response = requests.get(f"{url_all}?api_key={apikey}")
    except Exception as e:
        print(colored(e, "red"))
    data = response.json()
    spinner.stop()
    if response.status_code == 401:
        print(colored("Request Denied please enter correct API KEY", "red"))
    else:
        language_data = data["data"]["languages"]
        all_lang = []
        for dict in language_data:
            l = (Name, Percentage, Time_used) = (
                colored(dict["name"], "green"),
                colored(dict["text"], "blue"),
                colored(dict["percent"], "cyan"),
            )
            all_lang.append(list(l))
        spinner.stop()
        print(tabulate(all_lang, headers=["Name", "Time Used", "Percentage"]))
