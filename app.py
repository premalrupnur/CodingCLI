import argparse
import sys
from commands import allTimeSinceToday
from commands import codingGoals
from commands import dashboard
from commands import languageData
from termcolor import colored

def main():
    parser = argparse.ArgumentParser(prog='CodingCLI', usage='%(prog)s [options]',description='TO provide daily coding metrics')
    parser.add_argument('-a','--all',action='store_true',help='Displays All time since today')
    parser.add_argument('-l','--languages',action='store_true',help="Weekly status for each language")
    parser.add_argument('-p','--projects',action='store_true',help='Displays your project status')
    parser.add_argument('-k','--key',nargs=1,help='Enter your api key')
    parser.add_argument('-r','--remove',action='store_true',help='Removes your apikey')
    parser.add_argument('-g','--goals',action='store_true',help='Coding goals')
    args = parser.parse_args()
    print(colored('Welcome, Track your coding activities with CODINGCLI\n','magenta'))
    with open('API.txt',"r") as f:
        api_key = f.read()
    if(len(api_key)!=0 and not(args.remove)):
        if(args.all):
            allTimeSinceToday.allTime(api_key)
        if(args.languages):
            languageData.language(api_key)
        if(args.projects):
            project(api_key)
        if(args.goals):
            Codingoals.goal(api_key)
    if(api_key=='' and args.key):
        api_key = sys.argv[2]
        with open('API.txt',"w") as f:
            f.write(api_key)
        print('API KEY SAVED')
    if(args.remove):
        with open('API.txt',"w") as f:
            f.write('')
        print('API KEY REMOVED')
if __name__ == "__main__":
    main()  
