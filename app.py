from flask import Flask
from routes.alerts import alerts
app = Flask(__name__)

app.register_blueprint(alerts)