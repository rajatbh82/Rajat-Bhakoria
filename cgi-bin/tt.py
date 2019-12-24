#!/usr/bin/python3
print()

import os
import cgitb
cgitb.enable()
import time
from pynput.keyboard import Key , Controller as k
keyboard = k()
os.system("git add .")
os.system("git commit -m 'update'")
os.system("git push -u origin master &")
time.sleep(10)
keyboard.type("rajatbh82\n")
time.sleep(1)
keyboard.type("Rajat@20\n")
time.sleep(10)
keyboard.type("\n")
