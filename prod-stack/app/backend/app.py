from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "API jalan bro!"

@app.route("/db")
def db():
    conn = psycopg2.connect(
        host="db",
        database="appdb",
        user="appuser",
        password="apppass"
    )
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return f"Waktu dari DB: {result}"

app.run(host="0.0.0.0", port=5000)
