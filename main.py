import sys
import config.config as config
import discord
from discord import Webhook, RequestsWebhookAdapter
from datetime import date
import time
import requests

lat = sys.argv[1]
long = sys.argv[2]
substance = sys.argv[3]
amount = sys.argv[4]

if substance == "Adderall":
    thumburl = "https://i.imgur.com/RYI6VQR.png"
elif substance == "Caffeine":
    thumburl = "https://i.imgur.com/MAzpXNn.png"

client = Webhook.from_url(config.webhookurl, adapter=RequestsWebhookAdapter())
session = requests.Session()
today = date.today()
date = today.strftime("%y-%m-%d")
timestamp = time.strftime('%m/%d/%Y %I:%M:%S %p', time.localtime())
geourl = "https://www.google.com/maps/search/?api=1&query=" + str(lat) + "000" + "%2C" + str(long) + "000"

embeded=discord.Embed(title = substance + " intake recorded @ " + timestamp, color=discord.Color.blue())
embeded.set_author(name="Med Tracker", icon_url="https://i.imgur.com/W1qOCsP.png")
embeded.set_thumbnail(url = thumburl)
embeded.add_field(name = "**Where:**", value = geourl)
embeded.add_field(name = "**Details:**", value = "Amount: " + amount + "mg")

client.send(embed=embeded)