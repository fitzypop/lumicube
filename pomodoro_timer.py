# pomodoro_timer.py

# raise LEDS "up" the cube, like raising sea levels
# left and right rise together,
# Once left and right grid has reached the top,
# fill top panel in diamond pattern, starting from the user pointed away,
# towards the back of the cube.
#
# update: diamond pattern grid is complex, too much math for my liking
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


def title(color):
    display.set_all(black)
    display.scroll_text("pomodoro timer", color, black)
    display.scroll_text("written by fitzypop   >:p", random_colour(), black)


def kv_grid(level: int, color: int) -> dict:
    """Generate {(x,y): color} dict.

    left right panel ( x 0 - 15, y 0 - 7 )
    top panel: ( x 0 -7, y 8 - 15 )
    """
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
        display.set_leds(grid)
        time.sleep(0.3)
        if i == 16:
            break


def flicker(grid, n=3):
    i = 0
    while i < n:
        i += 1
        display.set_all(black)
        time.sleep(0.5)
        display.set_leds(grid)
        time.sleep(0.5)
    display.set_all(black)
    time.sleep(0.5)


def main():
    display.brightness = 20

    while True:
        # TODO: where would button presses go in this loop?
        color = random_colour()
        title(color)
        rising_timer(color)
        flicker(kv_grid(16, color))


if __name__ == "__main__":
    main()
