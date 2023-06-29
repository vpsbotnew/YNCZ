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

USER_SESSION = "BQE4_0UAbQeeA3m9KmAIhhapFsnDSkRc2iDDqzzfHZWZ7G36ESdBOgpEcDcrTNWFkOWlVHeWPJR3KxFAI7jo9KDSgPPm4hYzk54Qpc3zjEjjQCJ79QRBat7joCHmJngv91rTitCgP8pplOWy1OTTPAXFiu9Q06_yoyj4vDR8yzvUUDb3vtIy6uSvBziI1aX6bu9e7HuGK9A6GGB8g0bqLprJh9WoFHAXOmI9xU7lHWVD62X22aMpS318Zo5brSRE9NRJXn4lFU72NhRZSduIVX5p9UgBSUmTjBQzkVj_KhNDjCL2PFVNmvDcGg2hU7Tc629eMHgqQaDKhUQSEadePBfdaxpcdQAAAAFeEmwDAA"

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
