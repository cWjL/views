import time
from progressbar import ProgressBar
from random import randint

class vote():
    def __init__(self, tor, url, n, vote_id, log):
        self.tor_driver = tor
        self.url = url
        self.n = int(n)
        self.log = log

    def run(self):
        #TODO add vote stuff
        tmp = ""

'''
ng-click="currentQuestion.isEnabled && doSelect(answer, $index)

indexes are layed out from left to right, starting at 0 (i think)
'''
