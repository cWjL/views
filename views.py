#!/usr/bin/env python3
import colorama
from colorama import Fore, Style
import argparse,sys,time
#from src.mask import mask
from src.visits import visits

def main():
    b_prefix = "["+Fore.RED+"*"+Style.RESET_ALL+"] "
    g_prefix = "["+Fore.GREEN+"*"+Style.RESET_ALL+"] "

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", action='store',dest='visit_url',help='View this page a whole bunch of times')
    parser.add_argument("-p",action='store',dest='vote_url',help='Vote in this poll')
    parser.add_argument("-N",action='store',dest='num',help='Do it this many times')

    args = parser.parse_args()
    if not args.num:
        print(b_prefix+"You must enter the number of visits/votes you want")
        print(b_prefix+"Try again")
        sys.exit(1)
    elif args.visit_url and args.vote_url:
        print(b_prefix+"You can either vote or visit, not both")
        print(b_prefix+"Try again")
        sys.exit(1)
    elif not args.visit_url and not args.vote_url:
        print(b_prefix+"You must either vote or visit")
        print(b_prefix+"Try again")
        sys.exit(1)
        
    if args.visit_url and not args.vote_url:
        url_to_visit = args.visit_url
        url_to_vote = None
    elif args.vote_url and not args.visit_url:
        url_to_vote = args.vote_url
        url_to_visit = None
        
    num = args.num
    
    try:
        m = visits(args.num, url_to_visit, url_to_vote)
    except Exception as e:
        print(b_prefix+"Error: "+str(e))
        sys.exit(1)

    print(g_prefix+"Campaign complete")
    time.sleep(3)
    print(g_prefix+"Exiting")
    sys.exit(0)

def get_config():
    conf_lines = []
    with open('src/views.conf', 'r') as conf:
        all_conf_lines = conf.readlines()
        for line in all_conf_lines:
            if '#' not in line:
                conf = line.split(' ')
                conf_lines.append(conf[1].replace('\n', ''))
    return(conf_lines[0])

    

if __name__ == "__main__":
    colorama.init()
    main()
