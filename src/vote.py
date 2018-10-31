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
                
                for i in self.vote_id:
                    try:
                        button = browser.find_element_by_id(i)
                        button.click()
                    except:
                        button = browser.findElement(By.cssSelector(".submit.icon"))
                        button.click()
                    time.sleep(1)
                time.sleep(2)
                browser.close()
                time.sleep(randint(0,5))
                if self.tor_driver.swap_ident():
                    self.log.info('Swapping IP')
                else:
                    self.log.info('Swap IP failed')
            else:
                return False

        return True
        
'''
finds the button, but can't click it
button2 = browser.find_elements_by_xpath("//*[contains(text(), 'Vote')]")

'''
