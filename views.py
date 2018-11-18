#!/usr/bin/env python3
import colorama
from colorama import Fore, Style
import argparse,sys,time,os,logging,traceback
from src.visits import visits

def main(log_path):
    '''
    Either visit a webpage a whole bunch of times (to fake interest in a particular page), or vote in
    some online poll a bunch of times (currently limited to Strawpoll.me only).

    @author cWjL
    '''
    b_prefix = "["+Fore.RED+"*"+Style.RESET_ALL+"] "
    g_prefix = "["+Fore.GREEN+"*"+Style.RESET_ALL+"] "
    
    log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S', filename='logs/sec.log', filemode='w')

    log_path = ck_path(log_path)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", action='store',dest='visit_url',help='View this page a whole bunch of times')
    parser.add_argument("-p",action='store',dest='vote_url',help='Vote in this poll')
    parser.add_argument("-N",action='store',dest='num',help='Do it this many times')

    args = parser.parse_args()

    if not args.num:
        print(b_prefix+"You must enter the number of visits/votes you want")
        print(b_prefix+"Try again")
        log.error('Arugment error: no visit number')
        sys.exit(1)
    elif args.visit_url and args.vote_url:
        print(b_prefix+"You can either vote or visit, not both")
        print(b_prefix+"Try again")
        log.error('Arugment error: two modes selected, one required')
        sys.exit(1)
    elif not args.visit_url and not args.vote_url:
        print(b_prefix+"You must either vote or visit")
        print(b_prefix+"Try again")
        log.error('Arugment error: no mode specified')
        sys.exit(1)            
        
    if args.visit_url and not args.vote_url:
        url_to_visit = args.visit_url
        url_to_vote = None
    elif args.vote_url and not args.visit_url:
        url_to_vote = args.vote_url
        url_to_visit = None
        
    num = args.num
    
    try:
        log.info('Starting campaign')
        vis = visits(args.num, log, url_to_visit, url_to_vote)
        fate = vis.run()
    except Exception as e:
        print(b_prefix+"Error: "+str(e)+str(traceback.print_exc()))
        log.error('Exception:'+str(e))
        sys.exit(1)
    if fate == 0:
        print(g_prefix+"Campaign complete")
        log.info('Finished campaign.  Successful')

    else:
        print(b_prefix+"Campaign finished, but incomplete")
        log.info('Finished campaign.  Unsuccessful')
    time.sleep(2)
    print(g_prefix+"Exiting")
    sys.exit(0)

def ck_path(fp):
    '''
    Check file path format

    @param string filepath
    @return string formatted filepath
    '''
    if fp[len(fp)-1] == "\\" or fp[len(fp)-1] == "/":
        return fp
    else:
        if "\\" in fp:
            fp = fp + "\\"
        else:
            fp = fp + "/"
    return fp

def get_config():
    '''
    Get configuration file

    @param none
    @return list
    '''
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
    if not os.path.exists("logs"):
        os.makedirs("logs")
    main(os.path.abspath("logs"))
