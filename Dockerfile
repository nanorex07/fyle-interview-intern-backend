FROM python:3.8-slim

WORKDIR /application
COPY . /application

RUN pip install virtualenv
RUN virtualenv env --python=python3.8
RUN . env/bin/activate

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=core/server.py

RUN rm -f core/store.sqlite3
RUN flask db upgrade -d core/migrations/

EXPOSE 7755
CMD ["bash", "run.sh"]