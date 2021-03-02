FROM python

RUN mkdir /project

WORKDIR / project

COPY . /project

RUN pip install -r requierements.txt
