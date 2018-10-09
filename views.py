#!/usr/bin/env python3
import colorama
from colorama import Fore, Style
import argparse,sys
from src.mask import mask

def main():
    b_prefix = "["+Fore.RED+"*"+Style.RESET_ALL+"] "
    g_prefix = "["+Fore.GREEN+"*"+Style.RESET_ALL+"] "

    parser = argparse.ArgumentParser()
    parser.add_argument("-t",action='store',dest='tor_path',help='Path to start_tor_browser executable')
    parser.add_argument("-v", action='store',dest='visit_url',help='View this page a whole bunch of times')
    parser.add_argument("-p",action='store',dest='vote_url',help='Vote in this poll')
    parser.add_argument("-N",action='store',dest='num',help='Do it this many times')

    args = parser.parse_args()
    tor = None
    if not args.tor_path:
        print(b_prefix+"You must enter the file path to your start_tor_browser executable")
        print(b_prefix+"Try again")
        sys.exit(1)
    elif not args.num:
        print(b_prefix+"You must enter the number of visits/votes you want")
        print(b_prefix+"Try again")
        sys.exit(1)
    elif args.visit_url and args.vote_url:
        print(b_prefix+"You can either vote or visit, not both")
        print(b_prefix+"Try again")
        sys.exit(1)

    tor = mask(args.tor_path)

    print(g_prefix+"TEST")
    
    sys.exit(0)

if __name__ == "__main__":
    colorama.init()
    main()
