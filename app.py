import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('APP_SECRET')
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(data):
    message = data['message']
    emit('message', {'message': message}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)