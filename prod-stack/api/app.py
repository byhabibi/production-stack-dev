from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "API jalan bro!"

app.run(host="0.0.0.0", port=8000)
