FROM python:3.10

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app_weather .

ENTRYPOINT [ "python", "/app_weather/manage.py", "runserver" ]
