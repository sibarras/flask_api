from flask import Flask, request, jsonify
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return datetime.now().__str__()

def run():
    app.run(debug=True)
