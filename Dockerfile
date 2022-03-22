FROM python:3.7-alpine

WORKDIR /mnt

RUN pip install requests tweepy bs4
