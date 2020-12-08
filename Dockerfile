FROM python:latest

RUN apt-get update && apt-get install -y python3
RUN apt-get install -y python3-pip

COPY requirements.txt /
RUN pip install -r /requirements.txt

EXPOSE 5000

COPY . /

ENTRYPOINT ["python3"]
CMD ["app.py"]
