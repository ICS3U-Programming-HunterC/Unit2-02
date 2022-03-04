#!/usr/bin/env python3
# Created by: Hunter Connolly
# March 4
# This program calculates are and perimeter of a rectangle
# by asking the user for the length and width
import math


def main():
    # input
    print("Today we will calculate the area and")
    print("perimeter of a rectangle")
    length = int(input("Enter the length (mm): "))
    width = int(input("Enter the width (mm): "))

    # the process
    area = length * width
    perimeter = 2*(length + width)

    # output
    print("The area of this rectangle is: {} mm^2" .format(area))
    print("The perimeter is: {} mm" .format(perimeter))


if __name__ == "__main__":
    main()
