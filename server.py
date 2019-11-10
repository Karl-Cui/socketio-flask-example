from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
socketio = SocketIO(app)


# creating index page
@app.route('/')
def index():
    return render_template('index.html')


# handling a client connecting
@socketio.on('connect')
def test_connect():
    emit('test response', {'data': 'client connected!'})


# handling a client disconnecting
@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


# callback function to print whatever it receives
def print_callback(*args):
    print(args)


# handle user sending a message
@socketio.on('user message event')
def handle_test_event(json):
    print(json)
    socketio.emit('test response', json, callback=print_callback)


if __name__ == '__main__':
    socketio.run(app)
