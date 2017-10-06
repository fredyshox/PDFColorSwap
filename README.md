# PDFColorSwap

PDFColorSwap is a command line tool for color conversion of PDF files written in python. It can replace all occurrences of given color with another one.

It's very useful when there's a need to print something but the printer lacks or has low amount of black ink and has some color ink to spare. In this case swapping black color with for instance darker blue should get the job done. 

## Supported PDF ColorSpaces

* /DeviceRGB
* /DeviceCMYK
* /DeviceGray

Color conversion may not work correctly if pdf file is using different color spaces.

## Requirements

* Python 2.7 or newer
* PyPDF2 package (https://github.com/mstamy2/PyPDF2)

## Installation

* Download PDFColorSwap source
* Unpack it
* Run setup.py with command from its directory:
```
$ python setup.py install
```

## Usage

To use this tool, destination color hex string and path to input pdf file must be provided.
Color hex must contain 3 hexadecimal values corresponding to RGB color values (rrggbb).
Color hex can also be prefixed with #, but then it should be placed between pair of apostrophes ('#rrggbb')

### Examples
```
$ pdfcolor.py '#000066' input.pdf
// converts whole document from black to dark blue

$ pdfcolor.py -c '#101010' -o myOutput.pdf '#000066' input.pdf
// convert whole document from dark grey to dark blue and save as myOutput.pdf

$ pdfcolor.py -c '#101010' -p 0 -o myOutput.pdf '#000066' input.pdf
// convert only the first page from from dark grey to dark blue and save as myOutput.pdf
```

### Options

* [-o filename] 
* * Specifies the name of output file (default output.pdf)
* [-O path]             
* * Specifies the directory where output should be saved
* [-c color_hex]
* * Hex string of color that will be swapped (default black)
* [-p pageno pageno...]
* * Indexes of pages where conversion should occur
* [-P password]
* * Password to the input file if it's encrypted
