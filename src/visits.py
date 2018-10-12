import sys
from src.mask import mask
import colorama
from colorama import Fore, Style

class visits():
    def __init__(self, num, visit=None, vote=None):
        self.visit = visit
        self.vote = vote
        self.num = num
        self.tor_path = self._get_config()
        self._test_def()

    def _get_config(self):
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
