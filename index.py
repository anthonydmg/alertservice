from app import app, socketio

if(__name__ == "__main__"):
    socketio.run(app, host='0.0.0.0' , port=5055 ,debug= True)
    #app.run(host='0.0.0.0', port=5000 ,debug= True) 
