from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Farmer App Backend is running"}

@app.get("/prices")
def get_prices():
    return {
        "cotton": 42.5,
        "wheat": 18.3,
        "pistachio": 210.0,
        "currency": "USD/kg"
    }

@app.get("/weather")
def get_weather():
    return {
        "temperature": 28.4,
        "humidity": 55,
        "soil_moisture": 42,
        "sensor_count": 12
    }

@app.get("/alerts")
def get_alerts():
    return {
        "alerts": [
            {"type": "price", "message": "Cotton price dropped below threshold"},
            {"type": "weather", "message": "Low soil moisture detected on Farm 7"}
        ]
    }