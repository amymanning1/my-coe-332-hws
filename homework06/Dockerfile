FROM python:3.8.10

RUN pip install Flask==2.2.2
RUN pip install redis==4.5.1

ADD ./auto_trends_app.py /auto_trends_app.py
ADD ./auto-trends-manufacturer.csv /auto-trends-manufacturer.csv

CMD ["python", "auto_trends_app.py"]
