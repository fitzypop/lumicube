"""Show the current price of Bitcoin with color coded text.

Color meanings:
    - Green text: Sell
    - Blue text: HODL
    - Gold text: Buy and HODL
"""

from datetime import datetime, timedelta
import requests
import time
from contextlib import suppress
from copy import deepcopy

from money import Money  # pip install money

# Normal Price targets
# BUY_PRICE = 25_000
# SELL_PRICE = 60_000

# 3/9/24 - BTC hit $70k and is holding at $68k, need more fine grain targets
SELL_PRICE = 70_000
BUY_PRICE = 67_999

BLACK = 0x00000
BLUE = 0x0000FF
GOLD = 0xFFD700
GREEN = 0x00FF00
RED = 0xFF0000
WHITE = 0xFFFFFF

# clear all leds
display.set_all(BLACK)


def get_color(price):
    # Buy Color
    if price <= BUY_PRICE:
        color = GOLD

    # Hodl color
    elif BUY_PRICE < price < SELL_PRICE:
        color = BLUE

    # Sell color
    elif price >= SELL_PRICE:
        color = GREEN

    else:
        color = WHITE

    return color


def get_btc_price():
    # while True:
    #     with suppress(Exception):
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    price = response.json()["data"]["priceUsd"]
    m_price = Money(price, "USD").format("en_US")
    print(f"BTC {m_price} {start.strftime('%d-%m-%Y %H:%M:%S')}")
    return m_price, get_color(float(price))


if __name__ == "__main__":
    start = datetime.now()
    price, color = get_btc_price()
    wait_time = timedelta(minutes=0.5)

    while True:
        display.scroll_text(f"BTC {price}", speed=1.5, colour=color)

        if (now := datetime.now()) >= start + wait_time:
            start = deepcopy(now)
            price, color = get_btc_price()
        else:
            time.sleep(3)
