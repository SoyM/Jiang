#!/usr/bin/python
# -*- coding:utf-8 -*-

from Kernel import *
import re
import threading


def thread1():
    import temp

k = Kernel()
k.bootstrap(learnFiles=["en1.6/jiang.aiml", "self-test.aiml"])

# Run an interactive interpreter
print "\nEntering interactive mode (ctrl-c to exit)"
i = 1
while True:
    jiang = k.respond(raw_input("> "))
    if re.match("J", jiang):
        jiang = jiang[1:]
        file = open("temp.py", "w")
        file.write("import test\ntest." + jiang + "()")
        file = open("temp.py", "r")
        file.close()
        t = "t"+str(i)
        t = threading.Thread(target=thread1, name='thread-' + str(i))
        t.setDaemon(True)
        t.start()
        i += 1
        print i

    else:
        print(jiang)


