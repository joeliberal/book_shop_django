FROM python

WORKDIR /project

Run pip install -U pip

COPY requirements.txt /project

RUN pip install -r requirements.txt

COPY . /project

EXPOSE 8000

CMD ["gunicorn","mysite.wsgi","*:8000"]


#docker build -t shop_book:v1 .
#docker run -itd --net host --name project shop_book:v1