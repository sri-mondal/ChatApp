from flask import Flask, render_template
import os
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET")
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('message')
def message(data):
    send(data, broadcast=True)


if __name__ == "__main__":
    app.run()
