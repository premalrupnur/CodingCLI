import requests
import json
from tabulate import tabulate
from halo import Halo
from termcolor import colored


def goal(apikey: str):
    spinner = Halo(text="Requesting Data", spinner="dots")
    spinner.start()
    url_goals = "https://wakatime.com/api/v1/users/current/goals"
    try:
        response = requests.get(f"{url_goals}?api_key={apikey}")
    except Exception as e:
        print(colored(e,'red'))
    rawdata = response.json()
    l = []
    coding_goals = []
    if response.status_code == 401:
        print(colored("Request Denied please enter correct API KEY", "red"))
    else:
        for week, goal in enumerate(rawdata["data"][0]["chart_data"]):
            WeekNumber = "Week" + str(week)
            l = [
                colored(WeekNumber, "yellow"),
                colored(goal["range"]["start"], "cyan"),
                colored(goal["range"]["end"], "blue"),
                colored(goal["range_status_reason_short"], "magenta"),
            ]
            if goal["range_status"] == "Success" or goal["range_status"] == "ignored":
                l.append(colored(goal["range_status"], "green"))
            else:
                l.append(colored(goal["range_status"], "red"))
            coding_goals.append(l)
            l = []
        weekly_goal_hrs = colored(goal["goal_seconds_text"], "cyan")
        spinner.stop()
        print(colored(f"WEEKLY CODING GOAL:{weekly_goal_hrs}\n", "cyan"))
        print(tabulate(coding_goals, headers=["Week", "Start", "End", "ActualTime", "Status"]))
