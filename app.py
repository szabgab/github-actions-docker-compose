import os

from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

def get_mongodb():
    mongodb_host = os.environ.get("MONGODB_HOST")
    if not mongodb_host:
        exit("Missing MONGODB_HOST environment")
    dbname = os.environ.get("MONGODB_DATABASE")
    if not dbname:
        exit("Missing MONGODB_DATABASE")

    client = MongoClient("mongodb://{mongodb_host}", connectTimeoutMS=5000, socketTimeoutMS=5000)
    return client[ dbname ]

@app.route("/")
def main():
    return "main page"


@app.route("/mongodb", methods=['POST'])
def mongodb_post():
    text = request.form.get('text', '')
    db = get_mongodb()
    return text
    result = db.storage.insert_one({"text": text})
    return "done"

@app.route("/mongodb", methods=['GET'])
def mongodb_get():
    db = get_mongodb()
    result = db.packages.find()
    return "qqrq"
