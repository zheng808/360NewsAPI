from flask import Flask, request, jsonify
from mysql import Mysql, DATABASE
import os, csv
from csvparser import Parser
from rest_api import rest_api

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/unique-users')
def unique_users():
    device = request.args.get('device')
    os = request.args.get('os')
    return jsonify(rest_api().unique_users(os, device))

@app.route('/loyal-users')
def loyal_users():
    device = request.args.get('device')
    os = request.args.get('os')
    return jsonify(rest_api().loyal_users(os, device))
    
if __name__ == "__main__":
    parse = Parser()
    app.run(debug=True, host='0.0.0.0')