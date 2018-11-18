import time
from src.mask import mask
import colorama
from colorama import Fore, Style

class visits():
    '''
    Visits object
    '''
    def __init__(self, num, log, visit=None, vote=None):
        self.visit = visit
        self.vote = vote
        self.num = num
        self.log = log
        self.page_elems = None
        self.tor_path = self._get_config()

    def run(self):
        '''
        Run the campaign based on command options

        @param none
        @return integer status
        '''
        b_prefix = "["+Fore.RED+"*"+Style.RESET_ALL+"] "
        g_prefix = "["+Fore.GREEN+"*"+Style.RESET_ALL+"] "
        tor = mask(self.tor_path, g_prefix, b_prefix)

        if self.visit is not None:
            from src.visit import visit
            print(g_prefix+"Getting browser")
            vis = visit(tor, self.visit, self.num, self.log)
            time.sleep(1)
            print(g_prefix+"Done")
            time.sleep(2)
            print(g_prefix+"Starting visits")
            if vis.run():
                print(g_prefix+"Site visited "+self.num+" times, with "+self.num+" different IP addresses")
            else:
                print(b_prefix+"Something went wrong, check log for details")
                return 1
        else:
            if self.vote is not None:
                from src.vote import vote
                
                self.page_elems = self._how_to_id(g_prefix).split(',')

                print(g_prefix+"Getting browser")
                vot = vote(tor, self.vote, self.num, self.page_elems, self.log)
                time.sleep(1)
                print(g_prefix+"Done")
                time.sleep(2)
                print(g_prefix+"Starting votes")
                if vot.run():
                    print(g_prefix+"Voted "+self.num+" times, with "+self.num+" differernt IP addresses")
                else:
                    print(b_prefix+"Something went wrong, check log for details")
                    return 1
            else:
                return 1
        return 0

    def _how_to_id(self, g_prefix):
        '''
        Print instructions

        @param string formated prefix
        @return String or None
        '''
        print(g_prefix+"You need to provide the \"ID\" of the element you want to vote.")
        print(g_prefix+"Navigate to "+self.vote)
        print(g_prefix+"Find the voting item (button, option, etc.), right click on it and click \"Inspect Element\".")
        print(g_prefix+"Locate the id, it'll look something like the examples below:")
        print("\t\t<p class=\"row answer-text flex-auto flex-center ng-binding\">DO IT</p>")
        print("\t\t\tIn this case, the \"ID\" would be \"DO IT\"")
        print("\t\t<input name=\"options\" value=\"136886764\" id=\"field-options-one\" type=\"radio\">")
        print("\t\t\tIn this case, the \"ID\" would be \"field-option-one\"")
        print("\t\t<input name=\"options\" value=\"136886765\" id=\"field-options-two\" type=\"radio\">")
        print("\t\t\tIn this case, the \"ID\" would be \"field-option-two\"")
        res = input(g_prefix+"Enter the ID: ")
        if res is not None:
            return res
        return None

    def _get_config(self):
        '''
        Get configuration file

        @param none
        @return list
        '''
        conf_lines = []
        with open('src/views.conf', 'r') as conf:
            all_conf_lines = conf.readlines()
            for line in all_conf_lines:
                if '#' not in line:
                    conf = line.split(' ')
                    conf_lines.append(conf[1].replace('\n', ''))
        return(conf_lines[0])
