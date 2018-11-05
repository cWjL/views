import time,sys
from progressbar import ProgressBar
from random import randint

class vote():
    def __init__(self, tor, url, n, vote_id, log):
        self.tor_driver = tor
        self.url = url
        self.n = int(n)
        self.vote_id = vote_id # don't need this
        self.log = log
        self.target_id = self._get_vote_profile(self.url)

    def run(self):
        if self.target_id is not None:
            bar = ProgressBar()
            for _ in bar(range(self.n)):
                browser = self.tor_driver.get_tor_browser()
                if browser is not None:
                    browser.get(self.url)
                    buttons = []
                    for target in self.target_id:
                        if target[1] is not None:
                            # This is not a good way to accomplish this
                            # Need a way to automatically find the voting components and ask the
                            # user which ones they want to use
                            if target[0] == 0:
                                buttons.append(browser.find_element_by_id(target[1]))
                            elif target[0] == 1:
                                buttons.append(browser.find_element_by_name(target[1]))
                            elif target[0] == 2:
                                buttons.append(browser.find_element_by_xpath(target[1]))
                            elif target[0] == 3:
                                buttons.append(browser.find_element_by_tag_name(target[1]))
                            elif target[0] == 4:
                                buttons.append(browser.find_element_by_class_name(target[1]))
                            elif target[0] == 5:
                                buttons.append(browser.find_element_by_css_selector(target[1]))

                    for button in buttons:
                        button.click()
                        time.sleep(.5)
                        
                    browser.close()
                    
                    if self.tor_driver.swap_ident():
                        self.log.info('Swapping IP')
                    else:
                        self.log.info('Swap IP failed')
                        return False
                else:
                    return False

            return True

    def _get_vote_profile(self,site):
        '''
        Get vote profile

        vote_target elements:
            0:    site key word
            1:    selenium find option
            2:    button click order

        @param url
        @return tuple
        '''
        # This is not a good way to accomplish this
        # Need a way to automatically find the voting components and ask the
        # user which ones they want to use
        # This can only work if I ingest the page source as and parse for the elements of interest
        # Try this https://stackoverflow.com/questions/25756436/selenium-returns-a-page-source-in-which-all-tags-names-have-a0-prefixed-to-th
        vote_target = [
            ("strawpoll",((0,"field-options-whore"),(1,None),(2,"//button[@type='submit']"),(3,None),(4,None),(5,None))),
            ("megaphone",((0,None),(1,None),(2,None),(3,None),(4,None),(5,None)))
        ]

        for target in vote_target:
            if target[0][0] in site:
                return (target[1][0],target[1][2])
        return None
'''
found button and can click it
>>> button = driver.find_element_by_xpath("//button[@type='submit']")
>>> button.click()
>>> 

0 => driver.find_element_by_id
1 => driver.find_element_by_name
2 => driver.find_element_by_xpath
3 => driver.find_element_by_tag_name
4 => driver.find_element_by_class_name
5 => driver.find_element_by_css_selector
'''
