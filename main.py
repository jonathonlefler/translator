#!/usr/bin/env python3
#Lefler

import sys
import csv
import cv2
from PIL import Image, ImageDraw, ImageFont
#import Image
from matplotlib import pyplot as plt


def build_image_library():
    font = ImageFont.truetype('fonts/rounded-mgenplus-1m-medium.ttf', 15)
    with open('kana.csv', newline='') as csvfile:
        kanalist = csv.reader(csvfile, delimiter=',')
        for row in kanalist:
            for item in row:
                print(item)
                imagecreate = Image.new('RGB', font.getsize(item), (255, 255, 255))
                draw = ImageDraw.Draw(imagecreate)
                draw.text((0, 0), item, font=font, fill=(0, 0, 0))
                #imagecreate.show()
                imagecreate.save("resources/" + item + ".png")
                #sys.exit(0)


def main():
    build_image_library()
    '''#method = cv2.TM_SQDIFF_NORMED
    #method = cv2.TM_SQDIFF
    #method = cv2.TM_CCORR
    #method = cv2.TM_CCORR_NORMED
    #method = cv2.TM_CCOEFF
    method = cv2.TM_CCOEFF_NORMED

    target = cv2.imread('resources/あ.png')
    #target = cv2.imread('resources/き.png')

    raw = cv2.imread('raw.png')

    result = cv2.matchTemplate(target, raw, method)

    min, _, minlocation, _ = cv2.minMaxLoc(result)

    MPx, MPy = minlocation

    trows, tcols = target.shape[:2]

    cv2.rectangle(raw, (MPx, MPy), (MPx+tcols, MPy+trows), (0, 0, 255), 2)

    cv2.imshow('output', raw)

    cv2.waitKey(0)#'''


    #img = cv2.imread('raw.png', 0)
    img = cv2.imread('raw2.png', 0)
    img2 = img.copy()
    #template = cv2.imread('resources/き.png', 0)
    template = cv2.imread('resources/あ.png', 0)
    #template = cv2.imread('raw_template_a.jpg', 0)
    w, h = template.shape[::-1]

    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)
        # Apply template Matching
        #print(img.shape)
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        plt.show()#'''
    #image = Image.open("raw.png")
    #print(image.format, image.size, image.mode)
    #image.show()

    #imageTest = Image.new('RGB', (100, 100))
    #draw = ImageDraw.Draw(imageTest)

    #print(font.getsize("TEST"))
    #draw.text((50, 50), "TEST", font=font)
    #imageTest.show()
    sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
