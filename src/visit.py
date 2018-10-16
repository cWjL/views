import stem.process, time
from stem import Signal
from stem.control import Controller
from progressbar import ProgressBar
from random import randint

class visit():
    def __init__(self, tor, url, n):
        self.tor_driver = tor
        self.url = url
        self.n = int(n)
        self._run()

    def _run(self):
        bar = ProgressBar()
        for i in bar(range(self.n)):
            browser = self.tor_driver.get_tor_browser()
            if browser is not None:
                browser.get(self.url)
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                browser.close() # Close browser
                time.sleep(randint(0,5)) # Sleep random time 
                if self.tor_driver.swap_ident():
                    #TODO log ip swap
                    tmp = ""
                else:
                    #TODO log ip swap failure
                    tmp = ""
            else:
                return False
        return True
