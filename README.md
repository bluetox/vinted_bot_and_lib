
# VINTED BOT and LIB

This project aims to make vinted_bot developpement easier. This project holds a special place in my heart because it teached me a lot.


## Requirements

For this to work you will need to have those python libraries installed :
- `http.client`
- `re`
- `bs4` (Beautiful Soup)
- `socks`
- `json`

You will also need proxies, the bot supports tor running on port 9050 but also free proxies and authentication proxies.

## Installation

Install my-project with pip :

```bash
pip install -r requirements.txt
```

## How it works

This bot utilises the vinted api to first filter interresting items. 

All requests are routed trough the tor service on port 9050. 

Then gets the html of the item page to extract a maximum of 4 pictures. 

Then it sends another request to the api to get the seller's rating, comments... 

You will have to complete the config file.

The bot supports multiprocessing so it is possible to send data to multiple channels without loosing speed.

You will have to create a discord bot for which there is a tutorial included, and save the token.

