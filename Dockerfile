FROM python

RUN mkdir -p /usr/src/app && mkdir -p /var/log/gunicorn

VOLUME [ "/disk"]

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt

COPY ./conf/pip.conf /etc/pip.conf

RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY . /usr/src/app

ENV FLASK_ENV production

ENV UPLOAD_DEST /disk

ENV PORT 8000

EXPOSE 8000

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "run:application"]