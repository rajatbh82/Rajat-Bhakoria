import os
import time
from pynput.keyboard import Key , Controller as k
keyboard = k()
os.system("git add .")
os.system("git commit -m 'update'")
os.system("git push -u origin master &")
print("out")
time.sleep(10)
keyboard.type("rajatbh82 \n")
time.sleep(1)
keyboard.type("Rajat@20 \n")
