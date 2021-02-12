# -*- coding: utf-8 -*-

import cv2 as cv
import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

PDF = "PDF/image.pdf"
images = convert_from_path(PDF)
img_counter = 1

for i in range(len(images)):
    images[i].save("page"+str(i)+".jpg", 'JPEG')
    img_counter = img_counter + 1

limit_page = img_counter - 1
document = "text.txt"
f = open(document, 'w+')

for i in range(limit_page):
    print(i)
    file_png = "page"+str(i)+".jpg"
    img = cv.imread(file_png)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # ret, threshold_image = cv.threshold(gray, 0, 255, cv.THRESH_BINARY)
    # ret2, threshold_image2 = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
    threshold_image3 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    # medianBlur = cv2.medianBlur(gray, 5)

    file = "ch.png"
    cv.imwrite(file, threshold_image3)

    text = pytesseract.image_to_string(Image.open(file))
    os.remove(file)
    os.remove(file_png)
    f.write(text)
    # print(text)

    # cv.imshow('original', img)
    # cv.imshow('threshold', threshold_image3)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
f.close()
