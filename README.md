# weather-api-fastapi
A FastAPI weather service that fetches real-time weather data using wttr.in.

## Endpoints

**GET /weather?city=London**

Returns:
```json
{
  "city": "London",
  "temperature": "26",
  "humidity": "19",
  "weather": "Sunny"
}
```

## Setup
pip install fastapi uvicorn requests
uvicorn weather_api:app --reload

Visit: http://localhost:8000/weather?city=London

## Error Handling

- City not found: returns error message
- Network errors: caught and returned
