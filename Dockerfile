FROM python:3.10

COPY app_weather/requirements.txt .
RUN pip install -r requirements.txt

COPY app_weather/app_weather .

ENTRYPOINT ["python", "/app_weather/manage.py", "runserver"]
