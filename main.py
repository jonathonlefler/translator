#!/usr/bin/env python3
#Lefler

import sys
import csv
import cv2
from PIL import Image, ImageDraw, ImageFont
#import Image


def main():
    with open('kana.csv', newline='') as csvfile:
        kanalist = csv.reader(csvfile, delimiter=',')
        '''for row in kanalist:
            print(row)'''

    image = Image.new('RGB', (100, 100))
    draw = ImageDraw.Draw(image)
    draw.text((50, 50), "TEST", font=ImageFont.truetype(11))
    sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
