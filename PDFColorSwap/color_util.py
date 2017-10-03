#! /usr/bin/env python
#
# color_util.py
#
# Created by Kacper Raczy on 31.09.2017.
# Copyright (c) 2017 Kacper Raczy. All rights reserved.
#

"""
Color conversion functions working on colors from different color spaces.

Current supported cs's: RGB, CMYK, GrayScale
"""


def rgbToCMYK(r, g, b):
    """
    Converts RGB to CMYK
    :param r: red value (from 0.0 to 1.0)
    :param g: green value (from 0.0 to 1.0)
    :param b: blue value (from 0.0 to 1.0)
    :return: tuple containing CMYK color values (from 0.0 to 1.0 each)
    """
    k = 1-max([r,g,b])
    c = (1-r-k)/(1-k)
    m = (1-g-k)/(1-k)
    y = (1-b-k)/(1-k)
    return c,m,y,k


def cmykToRGB(c, m, y, k):
    r = (1-c)*(1-k)
    g = (1-m)*(1-k)
    b = (1-y)*(1-k)
    return r,g,b


def grayToRGB(grey):
    r = grey
    g = grey
    b = grey
    return r,g,b


def rgbToGray(r, g, b):
    """
    Converts RGB to GrayScale using luminosity method
    :param r: red value (from 0.0 to 1.0)
    :param g: green value (from 0.0 to 1.0)
    :param b: blue value (from 0.0 to 1.0)
    :return GreyScale value (from 0.0 to 1.0)
    """
    g = 0.21*r + 0.72*g + 0.07*b
    return g


def hexStringToRGB(hex):
    """
    Converts hex color string to RGB values
    :param hex: color string in format: #rrggbb or rrggbb with 8-bit values in hexadecimal system
    :return: tuple containing RGB color values (from 0.0 to 1.0 each)
    """
    temp = hex
    length = len(hex)
    if temp[0] == "#":
        temp = hex[1:length]
    if not len(temp) == 6:
        return None
    colorArr = bytearray.fromhex(temp)
    return colorArr[0], colorArr[1], colorArr[2]