FROM ubuntu:18.04

RUN apt-get update && apt-get install -y apt-utils && apt-get install -y curl && apt-get install -y poppler-utils \
    locales locales-all \
    tesseract-ocr \
    libtesseract-dev \
    python3.6 \
    python3-pip \
    libreoffice
    
RUN locale-gen ru_RU.UTF-8
ENV LANG ru_RU.utf8
ENV LANGUAGE ru_RU:ru
ENV LC_ALL ru_RU.UTF-8


ADD requirements.txt .

RUN python3.6 -m pip install pip --upgrade \
    && pip3.6 install -r requirements.txt

COPY ready /ready
COPY static /static
COPY templates /templates
COPY uploads /uploads
COPY mainprog.py /
COPY server.py /

EXPOSE 8080

CMD ["python3", "/server.py"]