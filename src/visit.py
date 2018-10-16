import stem.process, time
from stem import Signal
from stem.control import Controller
from progressbar import ProgressBar

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
                time.sleep(2)
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                if self.tor_driver.swap_ident():
                    #TODO log ip swap
                else:
                    #TODO log ip swap failure
            else:
                return False
        return True
