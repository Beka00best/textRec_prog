# Text Recognition Service
![Image alt](https://github.com/Beka00best/textRec_prog/blob/main/static/img/ocr.jpg)

This project highlights the text layer and OCR in pdf files and compares them.

## What is OCR?

Literally, OCR stands for Optical Character Recognition. It is a widespread technology to recognize text inside images, such as scanned documents and photos. OCR technology is used to convert virtually any kind of image containing written text (typed, handwritten, or printed) into machine-readable text data.

## What is it for?

This happens quite often, we want to understand whether OCR is needed or whether it is enough to use a text layer
The problem is that OCR is slow, so we don't want to use OCR on the whole document, but only part of it.

## Stages:
1. [Select text using ocr](#Select-text-using-ocr) :white_check_mark: 
2. [Select a text layer](#Select-a-text-layer) :white_check_mark: 
3. [Compare them (try to match and output mismatched strings) is the minimum](#Compare-them-(try-to-match-and-output-mismatched-strings)-is-the-minimum) :white_check_mark: 
4. [Write the launch instructions, put everything on github](#Write-the-launch-instructions,-put-everything-on-github) :white_check_mark: 
5. [Learn how to display diff beautifully](#Learn-how-to-display-diff-beautifully) :white_check_mark: 
6. [Wrap it all in a web service](#Wrap-it-all-in-a-web-service) :white_check_mark: 
7. [Learn how to pack it all in a container](#Learn-how-to-pack-it-all-in-a-container) :white_check_mark: 

### 1.Select text using ocr
For the convenience of the pdf file, I divided it into an image using the pdf2image library. And then selected the text with OCR using libraries such as [Tesseract](https://github.com/tesseract-ocr/tesseract), [OpenCV](https://github.com/opencv/opencv), [EasyOcr](https://github.com/JaidedAI/EasyOCR). OpenCV is needed for processing images that need to be pre-processed before we can pass the image to the OCR library. But according to the task, we should not do this because we just have a text.(Since I spent a lot of time studying the different noises in the images. I left this function but not applying it). Next, we have two very powerful tools in the face of Tesseract and EasyOcr. I used EasyOcr because for some reason Tesseract couldn't recognize the table.(But just like in the previous case, I wrote and left the function with Tesseract). Then all the recognized text is saved to a file.
### 2.Select a text layer
I learned about the [PyMuPDF](https://github.com/pymupdf/PyMuPDF) library, it has more functionality than the libraries that I used before. Using this library, I was able to select a text layer
### 3.Compare them (try to match and output mismatched strings) is the minimum
The comparison of two text selections and OCR goes something like this. To begin with, I go through each page, then through the text. First, I select the text of the minimum length from the text layer and look at the OCR, if there are more words in the OCR, then ***is displayed in red. Next, I look at the words and letters, if as in OCR, then green, otherwise red. In length, if the word is longer in the text layer, then I write red OCR, otherwise red *.
### 5.Learn how to display diff beautifully
[:arrow_up:3.Compare them (try to match and output mismatched strings) is the minimum](#3.Compare-them-(try-to-match-and-output-mismatched-strings)-is-the-minimum)
### 6.Wrap it all in a web service
The site is written in html and CSS.Located  in [index.html](#https://github.com/Beka00best/textRec_prog/blob/main/templates/index.html)
### 7.Learn how to pack it all in a container
The project is wrapped in docker
## Download
Install the dependencies
```sh
git clone https://github.com/Beka00best/textRec_prog.git
cd textRec_prog
```
### Docker
```sh
docker build -t prog .
```
Viewing images
```sh
docker images
```
### Run
```sh
docker run --rm --name server -p 5000:5000 prog
```
### Clean
```sh
docker rmi -f $(docker images -a -q)
```


### Other way
If you encounter problems with Docker, you can download it in a different way. You need to have a Linux system. In the terminal, enter the following commands:

```sh
Напишу потом
```

### How use website
After starting the server.py write in the browser:
```sh
http://localhost:5000/
```

You will be taken to this page:
***
![Image alt](https://github.com/Beka00best/textRec_prog/blob/main/static/img/01.png)
***
Then follow the instructions on the website