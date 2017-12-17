#!/usr/bin/env python

import itertools
import scrollphathd
from random import shuffle, randint

scrollphathd.set_brightness(0.9)

class Sparkle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reset()

    def run(self):
        if self.brightness >= self.speed:
            self.direction = -1

        if self.brightness <= 0:
            self.direction = 0

        self.brightness += self.direction
        return (self.x, self.y, float(self.brightness)/self.speed)

    def is_done(self):
        return self.brightness == 0

    def reset(self):
        self.brightness = 1
        self.direction = 1
        self.speed = randint(2, 50)


def main():
    pixels = itertools.product(
        range(scrollphathd.width), range(scrollphathd.height)
    )

    sparkles = [Sparkle(x,y) for x, y in pixels]
    shuffle(sparkles)

    active = []

    while True:

        if len(active) < 100:
            active.append(sparkles.pop(0))

        for s in active:
            scrollphathd.set_pixel(*s.run())

            if s.is_done():
                active.remove(s)
                s.reset()
                sparkles.insert(randint(0, len(sparkles)), s)

        scrollphathd.show()

# Catches control-c and exits cleanly
try:
    main()

except KeyboardInterrupt:
    scrollphathd.clear()
    scrollphathd.show()
    print("Exiting")

# FIN!
