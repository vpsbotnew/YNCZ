#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int("20512581")

API_HASH = "86e23f5f868190ca18c2a542247e51e6"

BOT_TOKEN = "5989078394:AAFX3-bU_4_8NeM8d2q2TEknJ_SCU45d9GI"

DB_URI = "mongodb+srv://ynmoviefilter:ynmoviefilter@cluster0.6erlpc6.mongodb.net/?retryWrites=true&w=majority"

USER_SESSION = "BQE4_0UAhpxbe3JgNsKvK3l0-Z_SOwi3TA1xPQUawZDZ5IOpe6lpLDXuvucA6Ve1IYxZv9Bx-hMmvDNFfm6Slg2BQzl9gAKWSOIdWP_yyL27zksnk3YoqoL7gz2CAoiGqo-MjJfrBNCOZQHuDZWt4QN0NinQjonRAtawBjeIhhSYqCxI10qx-eCCwMGtdHg8jP2xJ_Ym_OmgDBqv1kUjjsPBSbgy-bh4LVTKxM4bEtp8fEcJ05kssMuIzEwZZqVoKVMGPgqlY398EJ8za237GpqNMtlNynqcUV1wpj5KEajJC0exEud9zyyFgXFYokGQWLl1GGw-EguF1n-1iIt465KUtWl8zgAAAAFeEmwDAA"

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
