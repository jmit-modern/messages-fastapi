# messages-fastapi

RESTful API for SMS Inbox Users to send/receive the SMS messages

## Prerequisite

Python and Pip should be installed prior to the installation

## Installation

Install:

```
pip install -r requirements.txt
```

## Run server

Use `uvicorn` to run the server locally.

```
pip install uvicorn
uvicorn index:app --reload
```

It will run the web server on http://localhost:8000

## API Document

The swagger UI is ready for the API document on http://localhost:8000/docs or http://localhost:8000/redoc

## OS Requirements

Windows, MacOS, Linux
