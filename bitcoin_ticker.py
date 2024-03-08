"""Show the current price of Bitcoin with color coded text.

Color meanings:
    - Green text: Sell
    - Blue text: HODL
    - Gold text: Buy and HODL
"""

from datetime import datetime, timedelta
import requests
import math
from typing import Any

# clear all leds
display.set_all(black)

BUY_PRICE = 25_000
SELL_PRICE = 60_000


def parse_to_money(in_num: float) -> tuple[str, Any]:
    price_int = math.ceil(in_num)
    in_str = str(price_int)
    i_len = len(in_str)

    # Buy Color
    if price_int <= BUY_PRICE:
        color = 0xFFD700  # gold

    # Hodl color
    elif BUY_PRICE < price_int < SELL_PRICE:
        color = blue

    # Sell color
    elif price_int >= SELL_PRICE:
        color = green

    # shorten money string formatting
    if i_len == 7:
        price = f"{in_str[:1]}m"
    if i_len == 6:
        price = f"{in_str[:3]}k"
    elif i_len == 5:
        price = f"{in_str[:2]}k"
    elif i_len == 4:
        price = f"{in_str[:1]}k"
    else:
        price = in_str
    return price, color


def get_btc_price() -> tuple[str, Any]:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    price = float(response.json()["data"]["priceUsd"])
    return parse_to_money(price)


if __name__ == "__main__":
    price, color = get_btc_price()
    start = datetime.now()
    wait_time = timedelta(minutes=2)

    while True:
        display.scroll_text(f"BTC ${price}", speed=0.5, colour=color)

        if datetime.now() >= start + wait_time:
            price, color = get_btc_price()
            start = datetime.now()
