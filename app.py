from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs": 6,
        "category": "First private company to ISS",
        "word": "Spacex"
    },
    {
        "inputs": 7,
        "category": "Founder of INBO DIGITAL",
        "word": "Aravind"
    },

]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()
