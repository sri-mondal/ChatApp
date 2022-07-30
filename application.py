from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
secret_key = "sri"
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('message')
def message(data):
    send(data, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug=True)
