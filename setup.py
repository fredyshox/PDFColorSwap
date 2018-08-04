#! /usr/bin/env python
#
# setup.py
# Setup script
#
# Created by Kacper Raczy on 03.10.2017.
# Copyright (c) 2017 Kacper Raczy. All rights reserved.
#

from distutils.core import setup

pcg_version = "0.2.6"

setup(name="PDFColorSwap",
      version=pcg_version,
      description="PDF color conversion tool",
      long_description='''
      PDFColorSwap is a command line tool for color conversion of PDF files written in python. 
      It can replace all occurrences of given color with another one.''',
      author="Kacper Raczy",
      author_email="gfw.kra@gmail.com",
      install_requires=[
          "PyPDF2",
      ],
      packages=[
          "PDFColorSwap"
      ],
      scripts=[
          "tools/pdfcolor.py"
      ],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
          "Operating System :: OS Independent",
      ],
)