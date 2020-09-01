#!/usr/bin/python3
"""This displays “Hello HBNB!”"""
from flask import Flask


app = Flask(__name__)
app.run(host='0.0.0.0')

@app.route('/', strict_slashes=False)
def hello_world():
        print("Hello HBNB!")
        return 'Hello, World!'
