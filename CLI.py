from download import *
import os, sys
import json

with open("config.json", "r") as f:
	data = f.read()
f.close()
config = json.loads(data)

default_date = config["date"] or 0
default_country = config["country"] or 'cn'
save_path = config["save_path"] or "pic"
log_path = config["log_path"] or "bingbest.log"

date = input("Enter date: -1, 0, 1, 2, 3, 4, 5, 6. \n i means i days before today. \n Default: {date}\n".format(date = default_date)) or default_date
country = input("Enter country: ca, cn, fr, jp, nz, de, uk, us.\n Default: {country}\n".format(country = default_country)) or default_country
client = Downloader(date, country.lower())
client.get()
client.set()