# -*- coding: utf-8 -*-

import cv2 as cv
import os
import pytesseract
from PIL import Image

img = cv.imread('Image/7.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# ret, threshold_image = cv.threshold(gray, 0, 255, cv.THRESH_BINARY)
# ret2, threshold_image2 = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
# threshold_image3 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# medianBlur = cv2.medianBlur(gray, 5)
se = cv.getStructuringElement(cv.MORPH_RECT , (8,8))
bg = cv.morphologyEx(gray, cv.MORPH_DILATE, se)
out_gray = cv.divide(gray, bg, scale = 255)
out_binary = cv.threshold(out_gray, 0, 255, cv.THRESH_OTSU)[1] 

cv.imshow('binary', out_binary)  
# cv.imwrite('binary.png',out_binary)

cv.imshow('gray', out_gray)  
# cv.imwrite('gray.png',out_gray)
# file = 'ch.png'
# cv.imwrite(file, threshold_image3)

# text = pytesseract.image_to_string(Image.open(file))
# os.remove(file)
# print(text)
cv.imshow('gray_original', gray)
cv.imshow('original', img)
# cv.imshow('threshold', threshold_image3)
cv.waitKey(0)