import time
from progressbar import ProgressBar
from random import randint

class visit():
    def __init__(self, tor, url, n, log):
        self.tor_driver = tor
        self.url = url
        self.n = int(n)
        self.log = log

    def run(self):
        bar = ProgressBar()
        for _ in bar(range(self.n)):
            browser = self.tor_driver.get_tor_browser()
            if browser is not None:
                browser.get(self.url)
                time.sleep(2)
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                browser.close() # Close browser
                time.sleep(randint(0,5)) # Sleep random time 
                if self.tor_driver.swap_ident():
                    self.log.info('Swapping IP')
                else:
                    self.log.info('Swap IP failed')	
            else:
                return False
        return True
