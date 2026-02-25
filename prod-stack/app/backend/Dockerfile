FROM python:3.11-slim

WROKDIR /app

COPY requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
