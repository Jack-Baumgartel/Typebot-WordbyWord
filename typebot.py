"""Typebot text typer for MacOS, Windows, and Linux - Jack Baumgartel"""

import pyautogui
import time

pyautogui.FAILSAFE = True

starttime = 20

#Recieve message from user
#print('What is your message?\n')
message = input('What is your message?\n')

#Split the message into individual words
words = message.split()

#Recieve number of repetitions from user
repeats = int(input("How many times would you like to repeat this message?\n"))

#Instruct user on operation
print('\nOpen the location you wish to write your message, click in the type area, \nand wait! The program will start typing your message in {}s. To end the \nprogram, move your cursor quickly to any corner of your screen!'.format(starttime))

#Delay the start
time.sleep(starttime)

#Repeatedly type the message, pressing 'enter' in between each word
for j in range(repeats):
	for i in range(len(words)):
   	 pyautogui.typewrite(words[i])
   	 pyautogui.press("enter")







