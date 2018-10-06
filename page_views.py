#!/usr/bin/env python3
import stem.process
from stem import Signal
from stem.control import Controller
from splinter import Browser
import sys, os, subprocess

#check tor: netstat -ano | grep LISTEN | grep 9050
def main():
    if not check_tor():
        sys.exit(0)
    proxyIP = "127.0.0.1"
    proxyPort = 9150

    proxy_settings = {"network.proxy.type":1,
                      "network.proxy.ssl": proxyIP,
                      "network.proxy.ssl_port": proxyPort,
                      "network.proxy.socks": proxyIP,
                      "network.proxy.socks_port": proxyPort,
                      "network.proxy.socks_remote_dns": True,
                      "network.proxy.ftp": proxyIP,
                      "network.proxy.ftp_port": proxyPort
    }
    browser = Browser('firefox', profile_preferences=proxy_settings)
    browser.visit("http://www.icanhazip.com")

def check_tor():
    
    CMD = "netstat -ano | grep LISTEN | grep 9150"
    if(os.system(CMD) > 0):
        print("Not Bootstrapped")
        return False
    else:
        print("Bootstrap OK")
        return True

def start_tor(path=None):
    CMD = "start-tor-browser"
    start_cmd = ""
    if path is not None:
        start_cmd = path+CMD
    else:
        start_cmd = "/home/prole/Documents/tor/tor-browser_en-US/Browser/start-tor-browser"
        
    p = subprocess.Popen(start_cmd)

if __name__ == "__main__":
    main()
