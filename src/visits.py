import sys,os,time
from src.mask import mask
import colorama
from colorama import Fore, Style

class visits():
    def __init__(self, num, visit=None, vote=None):
        self.visit = visit
        self.vote = vote
        self.num = num
        self.tor_path = self._get_config()
        #self._test_def()
        self._run()

    def _run(self):
        b_prefix = "["+Fore.RED+"*"+Style.RESET_ALL+"] "
        g_prefix = "["+Fore.GREEN+"*"+Style.RESET_ALL+"] "
        print(g_prefix+"Starting TOR services")
        tor = mask(self.tor_path)
        time.sleep(3)
        print(g_prefix+"Starting TOR browser")
        browser = tor.get_tor_browser()
        time.sleep(5)

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

    def _test_def(self):
        print("good in visits")
        sys.exit(0)
