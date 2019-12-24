#!/usr/bin/python3
import time
from pynput.mouse import Button , Controller as m
print()
mouse = m()
mouse.position = (1163, 16)
time.sleep(1)
mouse.click(Button.left,1)
time.sleep(1)
mouse.position = (567, 696)
time.sleep(1)
mouse.click(Button.left,1)
from pynput.keyboard import Key , Controller as k
keyboard = k()
time.sleep(1)
keyboard.type("cd /home/zukz1/fuel_details/teleconsole \n")
time.sleep(1)
keyboard.type("./teleconsole > tele.txt \n")
