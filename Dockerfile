FROM python:3.9
WORKDIR /app
COPY weather_api.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["uvicorn", "weather_api:app", "--host", "0.0.0.0"]