FROM python:3.9.7

ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN python3 -m venv /opt/venv

COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt

COPY . .

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x entrypoint.sh

#CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["/app/entrypoint.sh"]

