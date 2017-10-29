#!/usr/bin/env python
# coding=utf-8
import sys
from time import sleep

from lifxlan import RED, WHITE, YELLOW, BLUE, GREEN, LifxLAN
from enum import Enum

class BuildStatus(Enum):
    SUCCESS = 1
    UNSTABLE = 2
    FAILED = 3
    ABORTED = 4

def build_color(status):
    colors = { 1: WHITE, 2: YELLOW, 3: RED, 4: BLUE }
    istatus = int(status)
    if istatus in colors:
        return colors[istatus]
    print("No color found for status {}".format(status))
    exit(2)

def main():
    # Knowing the number of bulbs in advance would make initial bulb discovery faster.
    print("Discovering lights...")
    lifx = LifxLAN()

    #if len(sys.argv) != 2:
    #    print("NO BUILD STATUS SPECIFIED")
    #    print("  python {} <build status>\n".format(sys.argv[0]))
    #    exit(1)

    status = sys.argv[1]

    # find device
    devices = lifx.get_lights()
    bulb = [x for x in devices if x.get_label() == "Bedroom Roof"]

    print("Found device: {}".format(bulb))
    if not bulb:
        print("No bulb found")
        return

    bulb = bulb[0]
    power = bulb.get_power()
    print(power)
    if power:
        print("Power is ON")
        print(bulb.get_color())
        target_color = build_color(status)
        bulb.set_color(target_color, 0.4)

if __name__=="__main__":
    main()
