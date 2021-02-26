FROM python:3.6

WORKDIR /home/bekzat/Beka/thirdsim/textRec_prog/

ADD program.py .

CMD ["python3", "./program.py"]