FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /cut_and_go
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
