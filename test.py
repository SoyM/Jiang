#!/usr/bin/python
# -*- coding:utf8 -*-
import time
import sys
import threading


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

if __name__ == "__main__":
    starttimed()
