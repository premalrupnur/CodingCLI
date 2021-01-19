import requests
import json
from termcolor import colored
from tabulate import tabulate
from halo import Halo


def project(apikey):
    spinner = Halo(text="Requesting Data\n", spinner="dots")
    spinner.start()
    url_projects = "https://wakatime.com/api/v1/users/current/projects"
    try:
        response = requests.get(f"{url_projects}?api_key={apikey}")
    except Exception as e:
        print(colored(e, 'red'))
    rawdata = response.json()
    if response.status_code == 401:
        spinner.stop()
        print(colored("Request Denied please enter correct API KEY", "red"))
    else:
        l = []
        projects = []
        for index, p in enumerate(rawdata["data"]):
            l = [
                colored(index, "yellow"),
                colored(p["created_at"], "blue"),
                colored(p["name"], "green"),
            ]
            projects.append(l)
            l = []
        spinner.stop()
        print(colored("Projects you worked on in this week:\n", "cyan"))
        print(tabulate(projects, headers=["SrNo", "Created_At", "Name"]))
