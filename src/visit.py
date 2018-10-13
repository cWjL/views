import stem.process, time
from stem import Signal
from stem.control import Controller

class visit():
    def __init__(self, tor, url):
        self.tor_driver = tor
        self.url = url
        self._run()

    def _run(self):
        for i in range(5):
            browser = self.tor_driver.get_tor_browser()
            browser.get(self.url)
            time.sleep(2)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
