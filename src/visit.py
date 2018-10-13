import stem.process
from stem import Signal
from stem.control import Controller

class visit():
    def __init__(self, tor, url):
        self.tor = tor
        self.url = url
