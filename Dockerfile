FROM python

ARG pypi_host=pypi.douban.com
ARG pypi_mirror=http://pypi.douban.com/simple

VOLUME [ "/disk"]

ENV LC_ALL C.UTF-8

ENV LANG C.UTF-8

ENV PIP_INDEX_URL $pypi_mirror

ENV FLASK_ENV production

ENV UPLOAD_DEST /disk

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt --trusted-host ${pypi_host}

COPY app app

COPY start_server.sh start_server.sh

COPY runner.py runner.py

RUN chmod a+x start_server.sh

EXPOSE 5000
ENTRYPOINT [ "./start_server.sh" ]