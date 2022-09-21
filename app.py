from flask import Flask
from flask_socketio import SocketIO, send, emit
from db.init import insertDataAlerDb
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
def fireDetected(data):
    print('Data: ', data)
    maxTemperature = data['maxTemperature']
    areaFire = str(data['areaFire']) + "m"
    latitud = str(data['latitud'])
    longitud = str(data['longitud'])
    altura =  str(data['distance'])
    print(maxTemperature)
    date = data['time']
    insertDataAlerDb(maxTemperature, latitud, longitud, altura, areaFire)
    print(date)
    emit('fireDetected',data, broadcast  = True)

@socketio.on('radarDistance')
def radarDistance(data):
    print("Data: ", data)