
from flask import Blueprint, jsonify, request, render_template

alerts  = Blueprint("alerts", __name__)

@alerts.route("/")
def home():
    return render_template('home.html')

@alerts.route("/registers")
def registers():
    return render_template('records.html')

@alerts.route('/api/alert', methods = ["POST"])
def alert():
    data = request.get_json()
    print(data)
    return jsonify(), 200