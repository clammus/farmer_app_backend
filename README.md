# Farmer App Backend

## Endpoints
- GET / — Health check
- GET /prices — Current crop prices
- GET /weather — Sensor data
- GET /alerts — Farmer alerts

## Deployment
Deployed on AWS Elastic Beanstalk (Python 3.14, us-east-1).

## Local Setup
pip install -r requirements.txt
uvicorn main:app --reload
