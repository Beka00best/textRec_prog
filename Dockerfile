FROM ubuntu:18.04
# RUN apt-get install -y python3.6

# RUN pip3 install -y python3-opencv
RUN apt-get update && apt-get install -y apt-utils && apt-get install -y curl && apt-get install -y poppler-utils \
    tesseract-ocr \
    libtesseract-dev \
    python3.6 \
    python3-pip 

RUN python3.6 -m pip install pip --upgrade && \
        python3.6 -m pip install wheel
RUN pip install opencv-python-headless 
RUN pip install pytesseract
RUN pip install pillow
RUN pip install pdf2image

RUN mkdir -p /test
ADD program.py /test/program.py
COPY /PDF/d.pdf /PDF/d.pdf

CMD ["python3", "/test/program.py"]