FROM python:3.8.10

RUN pip install Flask==2.2.2
#RUN pip install requests==2.22.0
RUN pip install DictReader==

COPY auto_trends_app.py /auto_trends_app.py

CMD ["python", "auto_trends_app.py"]
