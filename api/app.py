from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running!"

app.run(host="0.0.0.0", port=8000)
