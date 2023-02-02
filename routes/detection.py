
from flask import Blueprint, jsonify, request, render_template
import os 
from .controller import ControllerFFD

controllerFFD = ControllerFFD()

detection  = Blueprint("detection", __name__)
running = False

@detection.route("/detection/start", methods = ["POST"])
def start_fire_detection():
    print("Start Fire Detection")
    controllerFFD.run()
    running = True
    return jsonify(), 200


@detection.route("/detection/stop", methods = ["POST"])
def stop_fire_detection():
    print("Stop Fire Detection")
    controllerFFD.stop()
    running = False
    return jsonify(), 200
    
@detection.route("/detection/status", methods = ["POST"])
def status_fire_detection():
    return jsonify({ "running": running}), 200