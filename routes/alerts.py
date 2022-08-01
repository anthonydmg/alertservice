
from flask import Blueprint, jsonify, request

alerts  = Blueprint("alerts", __name__)

@alerts.route("/")
def home():
    return "Home"

@alerts.route('/api/alert', methods = ["POST"])
def alert():
    data = request.get_json()
    print(data)
    return jsonify(), 200