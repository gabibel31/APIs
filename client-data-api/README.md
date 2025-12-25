# Client Data Cleaning API

A simple REST API built with FastAPI to clean and validate client data.

## Features
- Accepts client data in JSON format
- Removes duplicate entries based on email
- Ignores incomplete data (missing email)
- Returns clean data with processing statistics
- Interactive API documentation via Swagger

## Tech Stack
- Python
- FastAPI
- Pydantic

## Example Use Case
This API can be used by companies to clean customer data coming from forms, CRMs or internal tools before storing or processing it.

## How to Run
```bash
python -m pip install fastapi uvicorn
python -m uvicorn main:app --reload
