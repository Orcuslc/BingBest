from download import *
import os, sys
import json

if not os.path.exists("config.json"):
	default_data = {
		"CLI": True,
		"date": 0,
		"country": "cn",
		"save_path": "pic",
		"log_path": "bingbest.log"
	}
	with open("config.json", "w") as f:
		json.dump(default_data, f)

with open("config.json", "r") as f:
	config = json.load(f)

is_CLI = config["CLI"]
default_date = config["date"]
default_country = config["country"]
save_path = config["save_path"]
log_path = config["log_path"]

if is_CLI:
	while 1:
		date = input("Enter date: -1, 0, 1, 2, 3, 4, 5, 6. \n i means i days before today. \n Default: {date}\n".format(date = default_date)) or default_date
		date = int(date)
		if date in [-1, 0, 1, 2, 3, 4, 5, 6]:
			break
	while 1:
		country = input("Enter country: ca, cn, fr, jp, nz, de, uk, us.\n Default: {country}\n".format(country = default_country)) or default_country
		if country in ["ca", "cn", "fr", "jp", "nz", "de", "uk", "us"]:
			break
	config["date"] = date
	config["country"] = country
else:
	date = default_date
	country = default_country

with open("config.json", "w") as f:
	json.dump(config, f)

client = Downloader(date, country.lower())
client.get()
client.set()