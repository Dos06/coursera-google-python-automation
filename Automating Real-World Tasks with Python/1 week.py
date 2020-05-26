#!/usr/bin/python3
import os
import glob
from PIL import Image

folder = '/home/student-04-22fb81da143e/images'


def reshape_icons():
    for file in glob.glob("ic_*"):
        img = Image.open(file)
        img = img.convert('RGB')
        img = img.rotate(90).resize((128, 128))
        new_file = "/opt/icons/" + file
        img.save(new_file, 'JPEG')


reshape_icons()
