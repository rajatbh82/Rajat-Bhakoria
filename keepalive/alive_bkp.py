import urllib.request as ur
import os
import time
from pynput.mouse import Button , Controller as m
from pynput.keyboard import Key , Controller as k
mouse = m()
keyboard = k()
link = open("link.txt",'r')
link = link.read()
link = link[:-1]
timeout = 1
while True:
	try:
		i = 0
		ur.urlopen(link+"/keepalive/",timeout=40)
		timeout = 1
		for i in range(0,120):
			time.sleep(1)
			print(i)
	except Exception as e:
		print(str(e)[:4])
		if str(e)[:4] == "HTTP":
			os.system("date >> date.txt")
			mouse.position = (1162, 16)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
			mouse.position = (803, 47)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
			mouse.position = (567, 696)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(2)
			keyboard.type("cd /home/android/fuel_details/keepalive \n")
			time.sleep(1)
			keyboard.type("ssh -R 80:localhost:80 ssh.localhost.run > localhost.txt \n")
			time.sleep(10)
			os.system("awk '{print $3}' localhost.txt > link.txt")
			link = open("link.txt",'r')
			link = link.read()
			link = link[:-1]
			mouse.position = (567, 696)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(2)
			keyboard.type("cd /home/android/fuel_details/git/rajatbh82.github.io \n")
			time.sleep(1)
			keyboard.type("echo '<!DOCTYPE html><html><head><title>HTML Meta Tag</title><meta http-equiv = \"refresh\" content = \"2; url = "+link+"\" /></head><body><p>Please Wait until your page is reached!!</p></body></html>' > index.html \n")
			time.sleep(1)
			mouse.position = (666, 700)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(5)
			keyboard.type("https://dcc.godaddy.com/manage/TESTYOURSITE.XYZ/dns\n")
			time.sleep(30)
			mouse.position = (1274, 634)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
			mouse.position = (1097, 377)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
			mouse.position = (991, 436)
			time.sleep(1)
			mouse.click(Button.right,1)
			time.sleep(1)
			mouse.position = (1094, 322)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
			keyboard.type(link[7:])
			print(link[7:])
			time.sleep(1)
			mouse.position = (1274, 634)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
			mouse.position = (810, 358)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(10)
			mouse.position = (1267, 45)
			time.sleep(1)
			mouse.click(Button.left,1)
			time.sleep(1)
		else:
			print(timeout)
			if timeout == 3:
				os.system("date >> date.txt")
				mouse.position = (1162, 16)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
				mouse.position = (803, 47)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
				mouse.position = (567, 696)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(2)
				keyboard.type("cd /home/android/fuel_details/keepalive \n")
				time.sleep(1)
				keyboard.type("ssh -R 80:localhost:80 ssh.localhost.run > localhost.txt \n")
				time.sleep(10)
				os.system("awk '{print $3}' localhost.txt > link.txt")
				link = open("link.txt",'r')
				link = link.read()
				link = link[:-1]
				mouse.position = (666, 700)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(5)
				keyboard.type("https://dcc.godaddy.com/manage/TESTYOURSITE.XYZ/dns\n")
				time.sleep(30)
				mouse.position = (1274, 634)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
				mouse.position = (1097, 377)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
				mouse.position = (991, 436)
				time.sleep(1)
				mouse.click(Button.right,1)
				time.sleep(1)
				mouse.position = (1094, 322)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
				keyboard.type(link[7:])
				print(link[7:])
				time.sleep(1)
				mouse.position = (1274, 634)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
				mouse.position = (810, 358)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(10)
				mouse.position = (1267, 45)
				time.sleep(1)
				mouse.click(Button.left,1)
				time.sleep(1)
			else:
				timeout = timeout+1
