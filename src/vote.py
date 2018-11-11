import time,sys
from progressbar import ProgressBar
from random import randint

class vote():
    def __init__(self, tor, url, n, page_elems, log):
        self.tor_driver = tor
        self.url = url
        self.n = int(n)
        self.page_elems = page_elems
        self.log = log
        self.target_id = self._get_vote_profile(self.url)

    def run(self):
        '''
        If vote_id is None, there is only one button to push in order to vote.
            Get self.target_id[1], use it as the button and click it.

        Otherwise, get self.vote_id as button and self.target_id as button.  Click the 
        first one first, then the second
        '''
        if self.target_id is not None:
            bar = ProgressBar()
            for _ in bar(range(self.n)):
                browser = self.tor_driver.get_tor_browser()
                if browser is not None:
                    browser.get(self.url)
                    
                    buttons = []

                    if target[1] is not None: # there should only be one target profile (returned from _get_vote_profile())
                        if target[0] == 1:
                            for elem in self.page_elems:
                                buttons.append(browser.find_element_by_id(elem)) # add the vote selections by ID
                                
                            buttons.append(browser.find_element_by_xpath(target[1])) # add the 'submit' button

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
            1:    vote button

        If vote button "id" is 0, use this in combination with the "vote_id" provided by
        the user, otherwise, if "id" is 1, use for both voting and submit (one-click votes)

        @param url
        @return tuple
        '''
        vote_target = [
            ("strawpoll",(0,"//button[@type='submit']")),
            ("megaphone",(1,None))
        ]

        for target in vote_target:
            return vote_target[0][1]
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
