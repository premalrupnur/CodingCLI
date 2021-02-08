import argparse
import os 
import sys
from commands import allTimeSinceToday
from commands import CodingGoals
from commands import languageData
from commands import projects
from termcolor import colored


def main():
    print(colored('Welcome, Track your coding activities with CODINGCLI\n','magenta'))
    parser = argparse.ArgumentParser(prog='CodingCLI', usage='%(prog)s [options]',description='TO provide daily coding metrics')
    parser.add_argument('-a','--all',action='store_true',help='Displays All time since today')
    parser.add_argument('-l','--languages',action='store_true',help="Weekly status for each language")
    parser.add_argument('-p','--projects',action='store_true',help='Displays your project status')
    parser.add_argument('-k','--key',nargs=1,help='Enter your api key')
    parser.add_argument('-r','--remove',action='store_true',help='Removes your apikey')
    parser.add_argument('-g','--goals',action='store_true',help='Coding goals')
    parser.add_argument('-d','--dashboard',action='store_true',help='Coding goals')
    args = parser.parse_args()
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(ROOT_DIR,'API.txt')
    with open(f'{path}',"r") as f:
        api_key = f.read()
    if(len(api_key)!=0 and not(args.remove)):
        if(args.all):
            allTimeSinceToday.allTime(api_key)
        if(args.languages):
            languageData.language(api_key)
        if(args.projects):
            projects.project(api_key)
        if(args.goals):
            CodingGoals.goal(api_key)
        if(args.dashboard):
            Dashboard.dashboard(api_key)
    if(api_key=='' and args.key):
        api_key = sys.argv[2]
        with open(f'{path}',"w") as f:
            f.write(api_key)
        print(colored('API KEY SAVED','green'))
    if(api_key=='' and len(sys.argv)!=1):
        print(colored("Please provide the API key",'red'))
    if(api_key!='' and args.remove):
        with open(f'{path}',"w") as f:
            f.write('')
        print(colored('API KEY REMOVED','green'))
if __name__ == "__main__":
    main()  
