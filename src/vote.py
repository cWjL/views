import stem.process, time
from stem import Signal
from stem.control import Controller
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
