from flask import Flask, request, jsonify
from pymongo import MongoClient
import logging

app = Flask(__name__)

def get_db():
  client = MongoClient(
      host='mongo',
      port=27017, 
      username='root', 
      password='pass',
      authSource='admin'
  )
  db = client["yummy"]
  collection = db["store"]

  return collection

@app.route('/')
def ping_server():
  return "YUMMY"

@app.route('/store')
def store_item():
  collection = get_db()
  doc = collection.insert_one({
     "item":request.args.get('item'),
     "count":request.args.get('count')
  })

  return f"Stored {request.args.get('count')} {request.args.get('item')}"

@app.route('/check')
def check_fridge():
  collection = get_db()
  check = collection.find_one({"item":request.args.get('item')})

  blah = {
     check["item"]:check["count"]
  }

  # return jsonify(blah)
  return "You have "+check["count"]+" "+check["item"]

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8001)

    client = MongoClient(
      host='mongo',
      port=27017, 
      username='root', 
      password='pass',
      authSource='admin'
    )
    db = client["yummy"]

# @app.route('/animals')
# def get_stored_animals():
#   db = get_db()
#   food = db.yummy_tb.find()
#   animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
#   return jsonify({"animals": animals})