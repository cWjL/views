import time,sys
from progressbar import ProgressBar
from random import randint

class vote():
    def __init__(self, tor, url, n, vote_id, log):
        self.tor_driver = tor
        self.url = url
        self.n = int(n)
        self.vote_id = vote_id
        self.log = log

    def run(self):
        bar = ProgressBar()
        for _ in bar(range(self.n)):
            browser = self.tor_driver.get_tor_browser()
            if browser is not None:
                browser.get(self.url)
                button = browser.find_element_by_id(self.vote_id)
                button.click()
                time.sleep(2)
                browser.close()
                time.sleep(randint(0,5))
                if self.tor_driver.swap_ident():
                    self.log.info('Swapping IP')
                else:
                    self.log.info('Swap IP failed')
            else:
                return False
        #print(self.vote_id)
        #sys.exit(0)
        return True
