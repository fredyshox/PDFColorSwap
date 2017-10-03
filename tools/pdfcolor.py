#
# pdfcolor.py
# pdfcolor swap
#
# Created by Kacper Raczy on 01.10.2017.
# Copyright (c) 2017 Kacper Raczy. All rights reserved.
#

from pdf_color import PdfColorConverter, RGBColor
from PyPDF2 import PdfFileReader
from color_util import hexStringToRGB
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description="Swaps colors of pdf file.")
    parser.add_argument("to_color", help="hex string of color that will replace")
    parser.add_argument("input", help="path to input pdf file", type=str)
    # optional arguments
    parser.add_argument("-p", help="page numbers", nargs="*", type=int, metavar="pageno", dest="pages")
    parser.add_argument("-P", help="password to pdf input file", metavar="password", nargs=1, dest="password", type=str)
    parser.add_argument("-c", help="color to be swapped(default black)", default="#000000", nargs=1, metavar="from_color", dest="from_color")
    parser.add_argument("-o", help="filename of output pdf", default="output.pdf", nargs=1, metavar="filename", dest="output")
    parser.add_argument("-O", help="save directory for output file(default current directory)", nargs=1, metavar="directory", dest="outputDir")
    args = parser.parse_args()

    # input path management
    currentPath = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(args.input):
        filepath = args.input
    else:
        input_filename = os.path.split(args.input)[1]
        filepath = currentPath + input_filename

    # opening the file with reader
    reader = PdfFileReader(filepath)
    if not args.password == None:
        reader.decrypt(args.password)

    colorWriter = PdfColorConverter()
    colorWriter.appendPagesFromReader(reader)

    # extracting colors
    from_rgb = hexStringToRGB(args.from_color)
    from_color = RGBColor(*from_rgb)
    to_rgb = hexStringToRGB(args.to_color)
    to_color = RGBColor(*to_rgb)

    # performing color swaps
    if args.pages!=None:
        for page in args.pages:
            if page>(colorWriter.getNumPages()-1):
                parser.error("page index to high: %d" % page)
                return 1
            else:
                colorWriter.swapColor(page, from_color, to_color)
    else:
        for page in range(0, colorWriter.getNumPages()):
            colorWriter.swapColor(page, from_color, to_color)

    # saving output pdf
    if args.outputDir==None:
        path = currentPath + '/' + args.output[0]
        outputStream = file(path, "wb")
    else:
        path = args.outputDir + args.output
        outputStream = file(path, "wb")

    colorWriter.write(outputStream)

    return 0

if __name__ == "__main__":
    main()