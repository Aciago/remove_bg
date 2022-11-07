#!/usr/bin/env python
# coding: utf-8

# # Background removal tool
# practice project from internet https://www.tomshardware.com/how-to/python-remove-image-backgrounds

# import libraries

from rembg import remove
from PIL import Image
import easygui as eg

# ask for a file to work with
input_path = eg.fileopenbox(title='Select image file')

# ask where to put resulting file
output_path = eg.filesavebox(title='Save file to..')

# remove bg
input = Image.open(input_path)

output = remove(input)

# create end file
output.save(output_path)