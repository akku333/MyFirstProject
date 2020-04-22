FROM python:3

ADD encrypt.py /

WORKDIR /user/src/app

COPY ./encrypt.py sample.json requirement.txt /user/src/app/
RUN pip install pystrich
RUN pip install pyAesCrypt
RUN python -m pip install --upgrade --user xmltodict

CMD [ "python", "./encrypt.py" ]
