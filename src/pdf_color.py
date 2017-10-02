#
# pdf_color.py
# PdfColorConverter
#
# Created by Kacper Raczy on 31.09.2017.
# Copyright (c) 2017 Kacper Raczy. All rights reserved.
#


from PyPDF2.pdf import PdfFileWriter, PdfFileReader,PageObject, ContentStream
from PyPDF2.utils import b_
from PyPDF2.generic import FloatObject, NameObject
from color_util import cmykToRGB, grayToRGB, rgbToCMYK
import os


class RGBColor(object):
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


class PdfColorConverter(PdfFileWriter):
    operators = [b_("sc"), b_("rg"), b_("g"), b_("k")]

    def swapColor(self, pageIndex, fromColor, toColor):
        """
        Substitutes all the color switching operators with fromColor with toColor.
        :param pageIndex: index of evaluated page
        :param fromColor: color which will be substituted
        :param toColor: destination color
        :return:
        """
        if pageIndex>=self.getNumPages():
            print("That page doesn't exist")
            return
        page = self.getPage(pageIndex)
        content = page["/Contents"].getObject()
        if not isinstance(content, ContentStream):
            content = ContentStream(content, page.pdf)

        for index, val in enumerate(content.operations):
            operands = val[0]
            operator = val[1]
            if operator == b_("cs"):
                print("nonstroking color space")
            elif operator in self.operators:
                if len(operands) == 3:
                    if self._evaluateColor3(operator, operands, fromColor):
                        print("probably rgb")
                        self._removeCSRef(content, index)
                        self._swapColorCmd(content, index, toColor)
                elif len(operands) == 1:
                    if self._evaluateColor1(operator, operands, fromColor):
                        print("probably grayscale")
                        self._removeCSRef(content, index)
                        self._swapColorCmd(content, index, toColor)
                elif len(operands) == 4:
                    if self._evaluateColor4(operator, operands, fromColor):
                        print("probably cmyk")
                        self._removeCSRef(content, index)
                        self._swapColorCmd(content, index, toColor)

        key = NameObject("/Contents")
        page[key] = content
        page.compressContentStreams()

    # removing operator that switches color space
    def _removeCSRef(self, content, index):
        if index >= 1 and content.operations[index - 1][1] == b_("cs"):
            content.operations.pop(index - 1)
            print("removingCS")
        return


    def _swapColorCmd(self, content, index, toColor):
        redObj = FloatObject((toColor.red / 255.0))
        greenObj = FloatObject((toColor.green / 255.0))
        blueObj = FloatObject((toColor.blue / 255.0))
        operator = b_("rg")
        content.operations[index] = ([redObj, greenObj, blueObj], operator)


    def _evaluateColor3(self, operator, operands, color):
        if operator == b_("sc") or operator == b_("rg"):
            red = int(operands[0] * 255)
            green = int(operands[1] * 255)
            blue = int(operands[2] * 255)
            if red == color.red and green == color.green and blue == color.blue:
                return True
        return False


    def _evaluateColor1(self, operator, operands, color):
        if operator == b_("sc") or operator == b_("g"):
            grey = int(operands[0] * 255)
            if grey == color.red and grey == color.green and grey == color.blue:
                return True
        return False

    def _evaluateColor4(self, operator, operands, color):
        if operator == b_("sc") or operator == b_("k"):
            cyan = operands[0]
            magenta = operands[1]
            yellow = operands[2]
            black = operands[3]
            (red, green, blue) = cmykToRGB(cyan, magenta, yellow, black)
            red = int(red * 255)
            green = int(green * 255)
            blue = int(blue * 255)
            if red == color.red and green == color.green and blue == color.blue:
                return True
        return False
