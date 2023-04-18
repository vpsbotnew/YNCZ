#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int("12158462")

API_HASH = "0b962717d931f4480c46d56c85d409a5"

BOT_TOKEN = "5989078394:AAFX3-bU_4_8NeM8d2q2TEknJ_SCU45d9GI"

DB_URI = "mongodb+srv://ynmoviefilter:ynmoviefilter@cluster0.6erlpc6.mongodb.net/?retryWrites=true&w=majority"

USER_SESSION = "BQCJnMPxcQiJl8mq0nwxcbbZjH2BwdNYrLvNU-R8BXkPgu3dd-e7T8ku5gzPAk_4_6Ti_lkx3DQqrWsZIYDRrx7d4l99d8oaGIIYviuiBzmSdCERYZP7BsVG1qBZEgppoInuE3F8vKIS_AlQGNwH1L89EJ7CTDyhLIl91TrcVtKuPksHSZgeMRCTn78A74oThhAlk5CXzENypMNmDflojVatwiPH9P0iQ5kAcnop8Q4fWDsPda-wCJmoapmEQMPHYylrkfFZJX2jC2LAdqHjZI1qbQcmg3suvxV6XHSPTJMa4cxUxj674oqVuo8qsXxD1dLg3LHjvSqpqY9JpdRbsrX0UFsxVQA"

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
