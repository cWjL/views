import sys,os,time
from src.mask import mask
import colorama
from colorama import Fore, Style

class visits():
    def __init__(self, num, log, visit=None, vote=None):
        self.visit = visit
        self.vote = vote
        self.num = num
        self.log = log
        self.tor_path = self._get_config()
        self._run()

    def _run(self):
        b_prefix = "["+Fore.RED+"*"+Style.RESET_ALL+"] "
        g_prefix = "["+Fore.GREEN+"*"+Style.RESET_ALL+"] "
        tor = mask(self.tor_path)
        # Get either visit or vote
        if self.visit is not None:
            from src.visit import visit
            print(g_prefix+"Starting site visits")
            if visit(tor, self.visit, self.num, self.log):
                print(g_prefix+"Site visited "+self.num+" times, with "+self.num+" different IP addresses")
            else:
                print(b_prefix+"Something went wrong, check log for details")
        else:
            from src.vote import vote
            # Do vote stuff
            # Need to pass it the tor object


    def _get_config(self):
        # Need to add file path format check.  Needs to end with a '\'
        # Maybe push config import to a seperate object
        conf_lines = []
        with open('src/views.conf', 'r') as conf:
            all_conf_lines = conf.readlines()
            for line in all_conf_lines:
                if '#' not in line:
                    conf = line.split(' ')
                    conf_lines.append(conf[1].replace('\n', ''))
        return(conf_lines[0])
