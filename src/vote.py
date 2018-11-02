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
        self.target_id = _get_vote_profile(self.url)

    def run(self):
        if self.target_id is not None:
            bar = ProgressBar()
            for _ in bar(range(self.n)):
                browser = self.tor_driver.get_tor_browser()
                if browser is not None:
                    browser.get(self.url)
                    time.sleep(1)
                    buttons = []
                    for target in self.target_id:
                        if target[1] is not None:
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
                        time.sleep(1)
                    
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
        vote_target = [
            ("strawpoll",((0,"field-options-one"),(1,None),(2,"//button[@type='submit']")(3,None)(4,None)(5,None)),(0, 2)),
            ("megaphone",((0,None),(1,None),(2,None)(3,None)(4,None)(5,None)))
        ]
        for target in vote_target:
            if target[0][0] in site:
                return (target[0][1],target[0][2])
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
