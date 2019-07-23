from flask import Flask
from flask_sockets import Sockets

from audio_sevice import AudioService,Tune
from utilities import x,y

app = Flask(__name__)
sockets = Sockets(app)

audio = AudioService()

@sockets.route('/accelerometer')
def echo_socket(ws):
    f = open("accelerometer.txt", "a")
    while True:
        message = ws.receive()
        # print(message)
        ws.send(message)
        print(message, file=f)
        message = message.split(",")

        # if round(float(message[0]),2) > 20 :
        #     print(round(float(message[0]),2),
        #           round(float(message[1]),2),
        #             round(float(message[2]),2))
        #
        #     audio.run_audio(Tune.HiHatOpen)

    f.close()


@sockets.route('/gyroscope')
def echo_socket(ws):
    f = open("gyroscope.txt", "a")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        # print(message, file=f)
    f.close()



@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    # server = pywsgi.WSGIServer(('192.168.0.107', 5000), app, handler_class=WebSocketHandler)
    server = pywsgi.WSGIServer(('10.170.31.249', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()