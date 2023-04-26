import webbrowser
import pyautogui
import time 

person_name = input('Enter the person name whom you want to send a message :')
my_msg= input("Enter your message:")

webbrowser.open('https://web.whatsapp.com/')

time.sleep(10)
#print(pyautogui.position())


pyautogui.click(2615,309)
pyautogui.typewrite(person_name)

time.sleep(5)


pyautogui.click(2603,393)


time.sleep(5)

pyautogui.typewrite(my_msg)

time.sleep(2)

pyautogui.click(4054,865)
