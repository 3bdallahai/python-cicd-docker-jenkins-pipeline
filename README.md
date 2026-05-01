# My Python CI/CD Project

## Overview
This project demonstrates a full CI/CD pipeline using Jenkins.

Pipeline stages:
- Build (install dependencies)
- Test (pytest)
- Dockerize application
- Run container
- Extract logs
- Fail pipeline on runtime errors

## Features
- Data cleaning and statistics computation
- Structured logging to file
- Dockerized application
- Jenkins pipeline with automated validation

## Run Locally

```bash
pip install -r requirements.txt
pytest
python app/main.py