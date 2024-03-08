from datetime import datetime, timedelta
import requests


def parse_to_money(in_str: str) -> str:
    i_len = len(in_str)

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
    return price


def get_btc_price() -> str:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    price = str(math.ceil(float(response.json()["data"]["priceUsd"])))
    return parse_to_money(price)


if __name__ == "__main__":
    price = get_btc_price()
    start = datetime.now()
    wait_time = timedelta(minutes=2)

    while True:
        display.scroll_text(
            f"BTC ${price}",
            speed=0.5,
            colour=0xFFD700,  # gold
        )

        if datetime.now() >= start + wait_time:
            print("updated")
            price = get_btc_price()
            start = datetime.now()
