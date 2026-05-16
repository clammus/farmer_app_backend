terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# AWS provider configuration
provider "aws" {
  region = "us-east-1"
}

# S3 bucket for storing farmer data
resource "aws_s3_bucket" "farmer_data" {
      bucket = "farmer-app-data"

  tags = {
    Name        = "Farmer App Data"
    Environment = "Production"
    Project     = "agri-coop-backend-data"
  }
}

# S3 bucket versioning
resource "aws_s3_bucket_versioning" "farmer_data" {
  bucket = aws_s3_bucket.farmer_data.id

  versioning_configuration {
    status = "Enabled"
  }
}