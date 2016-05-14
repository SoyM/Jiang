#!/usr/bin/python
# -*- coding:utf-8 -*-

from Kernel import *
import re
import threading


class MyThread(threading.Thread):
    def __init__(self, jiang):
        threading.Thread.__init__(self)
        self.jiang = jiang

    def run(self):
        # print "I am %s" % self.name
        if re.match("J", self.jiang):
            self.jiang = self.jiang[1:]
            import temp
            file = open("temp.py", "w")
            file.write("from test import " + self.jiang + "\n\n\ndef jiang():\n"+"\t" + self.jiang + "()\n")
            # file = open("temp.py", "r")
            file.close()
            reload(temp)
            temp.jiang()
        else:
            print(self.jiang)


if __name__ == "__main__":
    k = Kernel()
    k.bootstrap(learnFiles=["en1.6/jiang.aiml", "self-test.aiml"])
    lock = threading.Lock()
    print "\nEntering interactive mode (ctrl-c to exit)"
    i = 0
    while True:
        jiang = k.respond(raw_input("> "))
        my_thread = MyThread(jiang=jiang)
        my_thread.start()

        # print "current has %d threads" % (threading.activeCount())
        ThA = threading.enumerate()
        for d in range(len(ThA)):
            print ThA[d]
        i += 1
        print i






