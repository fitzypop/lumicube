# Pomodoro Timer

# raise LEDS "up" the cube, like raising sea levels
# left and right rise together,
# Once left and right grid has reached the top,
# fill top panel in diamond pattern, starting from the user pointed away, towards the back of the cube
#
# Concept: "Rising Timer"
# Amount of time passed = rising led levels
# colors:
#   red - work
#   green - short break
#   yellow ? - long break
#   white - lunch break (?)
#
# Need to figure out a way to calculate led levels based on time passed
#
# Focus Time Timer:
# Need to get current time, add 20 minutes
# raise red level over 20 minute span of time
#
# Short Break Timer:
# After 20 minutes, make beep or sound of some kind
# start green raising levels, over 1 - 5 minutes
#
# Long Break Timer:
# after three cycles of red and green, do 10 - 20 minute rising timer
#
# Lunch Break Timer:
# Not sure if I need this
# After 3 - 4 Long Breaks (i.e. hours), take 1 hour lunch break
# What color? White? Magenta?


import random
import time
from datetime import datetime
from pprint import pprint

from dateutil.relativedelta import relativedelta

# Initial Setup / Global things
time_format = "%H:%M:%S"


def kv_grid(level: int, color: int):
    # left - right x 0 - 15, y 0 - 7
    # top panel goes x 0 -7, y 8 - 15
    leds = dict()
    for x in range(16):
        for y in range(level):
            # top panel only needs x 0 - 7
            # no need to compute more
            if y > 7 and x > 7:
                continue
            leds[x, y] = color
    return leds


def rising_timer(color: int):
    i = 0
    while True:
        i += 1
        grid = kv_grid(i, color)
        # pprint(grid)
        display.set_leds(grid)
        time.sleep(0.3)
        if i == 16:
            return


def main():
    colors = [
        blue,
        cyan,
        green,
        grey,
        magenta,
        orange,
        pink,
        purple,
        red,
        white,
        yellow,
    ]

    display.scroll_text("pomodoro timer", magenta, black)

    while True:
        display.set_all(black)
        color = random.choice(colors)
        rising_timer(color)

    # TODO: 16 grid levels - 20 - 30 minute runtime, 2 - 5 minute runtime


if __name__ == "__main__":
    main()
