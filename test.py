#!/usr/bin/python
# -*- coding:utf8 -*-
import time
import sys
import win32api
import requests
import os


def warn():
    print('where you in\n where are you from\n where are you go\nvalue')


def gettime():
    print time.strftime('%Y-%m-%d %X', time.localtime())

def getweather():
    print("weather will coming soon.")

def starttimed():
    starttime = time.time()
    while True:
        endtime = time.time() - starttime
        endtime = round(endtime, 2)
        sys.stdout.write(str(endtime)+'\r')
        time.sleep(0.001)

def openbrowser():
    win32api.ShellExecute(0, 'open', 'http://', "", " ", 1)

def openchrome():
    win32api.ShellExecute(0, 'open', 'chrome.exe', "", " ", 1)

def verifycampus():
    # sys.path.append('tessdata/')
    # import logincampus
    # logincampus.logincampus()
    os.system(r"python C:\Users\SoyMilk\Desktop\pyAIML-master\tessdata\logincampus.py")
if __name__ == "__main__":
    verifycampus()
