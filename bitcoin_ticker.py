"""Show the current price of Bitcoin with color coded text.

Color meanings:
    - Green text: Sell
    - Blue text: HODL
    - Gold text: Buy and HODL
"""

from datetime import datetime, timedelta
import requests
import math
import time
from typing import Any


BUY_PRICE = 25_000
SELL_PRICE = 60_000

BLACK = 0x00000
BLUE = 0x0000FF
GOLD = 0xFFD700
GREEN = 0x00FF00
RED = 0xFF0000
WHITE = 0xFFFFFF

# clear all leds
display.set_all(BLACK)


def parse_to_money(in_num: float) -> tuple[str, Any]:
    price_int = math.ceil(in_num)
    in_str = str(price_int)
    i_len = len(in_str)

    # Buy Color
    if price_int <= BUY_PRICE:
        color = GOLD

    # Hodl color
    elif BUY_PRICE < price_int < SELL_PRICE:
        color = BLUE

    # Sell color
    elif price_int >= SELL_PRICE:
        color = GREEN

    # money string formatting
    if i_len == 7:
        price = f"${in_str[:1]}m"
    if i_len == 6:
        price = f"${in_str[:3]}k"
    elif i_len == 5:
        price = f"${in_str[:2]}k"
    elif i_len == 4:
        price = f"${in_str[:1]}k"
    else:
        price = in_str
    return price, color


def get_btc_price() -> tuple[str, Any]:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    price = float(response.json()["data"]["priceUsd"])
    print(f"BTC ${price:.2f}  {start}")
    return parse_to_money(price)


# TODO: 8x8 arrays for top panel display

buy = [
    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
]

if __name__ == "__main__":
    start = datetime.now()
    price, color = get_btc_price()
    wait_time = timedelta(minutes=2)

    while True:
        # display.set_panel("top", buy)
        display.scroll_text(f"BTC {price}", speed=1.5, colour=color)

        if datetime.now() >= start + wait_time:
            start = datetime.now()
            price, color = get_btc_price()
        else:
            time.sleep(3)
