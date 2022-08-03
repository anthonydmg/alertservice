from flask import Flask
from flask_socketio import SocketIO, send, emit

from routes.alerts import alerts
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.register_blueprint(alerts)

socketio = SocketIO(app, manage_session  = True)

@socketio.on('startFireDetection')
def startFireDetection(msg):
    print('Message: ' + msg)
    emit('startFireDetection',msg, broadcast  = True)

@socketio.on('stopFireDetection')
def stopFireDetection(msg):
    print('Message: ' + msg)
    emit('stopFireDetection',msg, broadcast  = True)

@socketio.on('fireDetected')
def startFireDetection(data):
    print('Message: ' + data)
    emit('fireDetected',data, broadcast  = True)
