import sys,os,subprocess,time,selenium
from selenium.webdriver.firefox.options import Options
import stem.process
from selenium import webdriver
from stem.control import Controller
from stem import Signal
from random import randint

class mask():
    '''
    Mask object
    '''
    def __init__(self, path, g_prefix, b_prefix):
        self.g_prefix = g_prefix
        self.b_prefix = b_prefix
        self.path = path
        self.opts = Options()
        self.opts.add_argument('-private')      
        
    def _check_tor(self):
        '''
        Checks for running TOR browser

        Only works on Linux based systems

        @param none
        @return boolean status
        '''
        CMD = "netstat -ano | grep LISTEN | grep 9150 > /dev/null 2>&1"
        if(os.system(CMD) > 0):
            return False
        else:
            return True
        
    def _start_tor(self):
        '''
        Start TOR browser

        @param none
        @return boolean status
        '''
        CMD = "start-tor-browser"
        try:
            p = subprocess.Popen(self.path+CMD)
        except:
            return False
        while True: # Give TOR browser time to open
            if self._check_tor():
                break
            else:
                time.sleep(2)
        return True

    def _get_ua(self):
        '''
        Get random user agent string

        @param none
        @return String
        '''
        ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
              "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
              "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",
              "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
              "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G570Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36",
              "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
              "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N910F Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36",
              "Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7",
              "Mozilla/5.0 (Linux; Android 7.0; HTC 10 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36",
        ]
        return ua[randint(0, (len(ua)-1))]

    def _get_tor_browser_profile(self):
        '''
        Get TOR browser profile

        @param none
        @return selenium webdriver
        '''
        profile = webdriver.FirefoxProfile()
        proxyIP = "127.0.0.1"
        proxyPort = 9150
        profile.set_preference("network.proxy.type", 1)  
        profile.set_preference("network.proxy.socks",proxyIP)
        profile.set_preference("network.proxy.socks_port",int(proxyPort))
        profile.set_preference("network.proxy.socks_remote_dns",True)
        profile.set_preference("browser.privatebrowsing.autostart",True)
        
        return profile

    def _get_proxy_list(self):
        ##############################################################################
        ####################### INCOMPLETE ##########################################
        #############################################################################
        '''
        Get up-to-date list of free proxy server IP:PORT, return it as a list
        to cycle through.

        OPTIONS:  Return the list of proxies, or return a webdriver using each 
        proxy....

        Not sure yet
        '''
        URI = "https://free-proxy-list.net/"

    
    def get_tor_browser(self):
        '''
        Get firefox browser using TOR proxy

        @param none
        @return selenium webdriver
        '''
        if not self._check_tor():
            print(self.g_prefix+"TOR not running, starting TOR")
            time.sleep(2)
            if not self._start_tor():
                print(self.b_prefix+"Could not start TOR browser")
                return None
            else:
                print(self.g_prefix+"TOR started successfully")
        return webdriver.Firefox(self._get_tor_browser_profile(),firefox_options=self.opts)
    
    def swap_ident(self):
        '''
        Swap TOR browser identity

        @param none
        @return boolean status
        '''
        if self._check_tor():
            with Controller.from_port(port=9151) as controller:
                controller.authenticate()
                controller.signal(Signal.NEWNYM)
                time.sleep(1) # Give the identity time to reset
            return True
        return False       
