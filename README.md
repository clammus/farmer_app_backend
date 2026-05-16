# Farmer App Backend

## Endpoints
- GET / — Health check
- GET /prices — Current crop prices
- GET /weather — Sensor data
- GET /alerts — Farmer alerts

## Cloud Deployment
- **Platform:** AWS Elastic Beanstalk (Python 3.14, us-east-1)
- **URL:** http://farmer-app-env.eba-meid6jwj.us-east-1.elasticbeanstalk.com
- **Storage:** AWS S3 bucket (farmer-app-data) with sensor data
- **Monitoring:** CloudWatch alarm on CPUUtilization > 80%
- **IaC:** S3 bucket provisioned via Terraform (see main.tf)

## Local Setup
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Infrastructure as Code
S3 bucket is provisioned with Terraform:
```bash
terraform init
terraform apply
```

## Project Structure
- `main.py` — FastAPI application
- `requirements.txt` — Python dependencies
- `Procfile` — Beanstalk startup command
- `main.tf` — Terraform IaC for S3 bucket
- `sensor_data.json` — Sample IoT sensor data