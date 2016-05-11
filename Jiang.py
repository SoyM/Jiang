#!/usr/bin/python
# -*- coding:utf-8 -*-

from Kernel import *
import re
import threading


def thread1():
    from temp1 import jiang
    jiang()
def thread2():
    from temp2 import jiang
    jiang()
def thread3():
    from temp3 import jiang
    jiang()
k = Kernel()
k.bootstrap(learnFiles=["en1.6/jiang.aiml", "self-test.aiml"])
mutex = threading.Lock()
# Run an interactive interpreter
print "\nEntering interactive mode (ctrl-c to exit)"
i = 1
while True:
    jiang = k.respond(raw_input("> "))
    if re.match("J", jiang):
        jiang = jiang[1:]
        t = "t"+str(i)
        if t == 't1':
            file = open("temp1.py", "w")
            file.write("from test import " + jiang + "\n\n\ndef jiang():\n"+"\t" + jiang + "()\n")
            # file = open("temp1.py", "r")
            file.close()
            mutex.acquire()
            t = threading.Thread(target=thread1, name='t' + str(i))
            t.setDaemon(False)
            t.start()
            mutex.release()
        elif t == 't2':
            file = open("temp2.py", "w")
            file.write("from test import " + jiang + "\n\n\ndef jiang():\n"+"\t" + jiang + "()\n")
            # file = open("temp2.py", "r")
            file.close()
            mutex.acquire()
            t = threading.Thread(target=thread2, name='t' + str(i))
            t.setDaemon(False)
            t.start()
            mutex.release()
        elif t == 't3':
            file = open("temp3.py", "w")
            file.write("from test import " + jiang + "\n\n\ndef jiang():\n"+"\t" + jiang + "()\n")
            # file = open("temp3.py", "r")
            file.close()
            t = threading.Thread(target=thread3, name='t' + str(i))
            t.setDaemon(False)
            t.start()
        print(t.isAlive())
        print "current has %d threads" % (threading.activeCount() - 1)
        ThA = threading.enumerate()
        for d in range(len(ThA)):
            print ThA[d]

    else:
        print(jiang)


