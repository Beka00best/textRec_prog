# -*- coding: utf-8 -*-
import cv2 as cv
import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import numpy as np
import easyocr
import fitz


def textFromPDF(doc):
  text = ''
  for page in doc:
    text = text + page.get_text()
  return text

def doImage(doc, pageNum):
  images = convert_from_path(doc)
  for i in range(len(images)):
    images[i].save("page"+str(i)+".jpg", 'JPEG')
  
def deleteImage(pageNum):
  for i in range(pageNum):
    file_png = "page"+str(i)+".jpg"
    os.remove(file_png)

def textFromPDF_OCR_1(doc, pageNum):
  allText = ''
  for i in range(pageNum):
    file_png = "page"+str(i)+".jpg"
    img = cv.imread(file_png)
    text = pytesseract.image_to_string(Image.open(file_png))
    allText = allText + text
    os.remove(file_png)
    write2doc(doc, text)
  return allText

def text_EASYOCR(IMAGE_PATH):
  reader = easyocr.Reader(['en', 'ru'], gpu = False)
  result = reader.readtext(IMAGE_PATH)
  text = ''
  for detection in result:
    text = text + ' ' + detection[1]
  return text

def doGoodImage(IMAGE_PATH, pageNum):
  img = cv.imread(IMAGE_PATH)
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  se = cv.getStructuringElement(cv.MORPH_RECT , (8,8))
  bg = cv.morphologyEx(gray, cv.MORPH_DILATE, se)
  out_gray = cv.divide(gray, bg, scale = 255)
  out_binary = cv.threshold(out_gray, 0, 255, cv.THRESH_OTSU)[1]
  file_png = "page"+str(pageNum)+".jpg"
  cv.imwrite(file_png, out_gray)


def write2doc(document, text):
  with open(document, 'w+') as f:
    f.write(text)


file = os.listdir('PDF')
PDF = 'PDF/' + file[-1]
pdfDocument = fitz.open(PDF)
pageNum = pdfDocument.pageCount - 1
textPDF = ''
textOCR = ''
textDiff = ''
document = "ready/text.txt"

textPDF = textFromPDF(pdfDocument)
# write2doc(document, textPDF)

# for i in range(pageNum):