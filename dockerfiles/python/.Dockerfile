FROM python:3.10.9

RUN python3.10 -m venv /opt/ve_ioet

COPY . /app/

RUN /opt/ve_ioet/bin/pip install -r /app/requirements.txt


