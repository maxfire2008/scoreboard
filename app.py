import CONFIG
import flask
import flask_socketio

app = flask.Flask(__name__)

app.config['SECRET_KEY'] = CONFIG.SECRET_KEY
socketio = flask_socketio.SocketIO(app)


@app.route("/view/<game>")
def view(game):
    return flask.render_template("view.html", game=game)

@socketio.on('join')
def on_join(data):
    room = data
    flask_socketio.join_room(room)


@socketio.on('leave')
def on_leave(data):
    room = data['room']
    flask_socketio.leave_room(room)


@app.route("/update/<game>", methods=['POST'])
def update(game):
    flask_socketio.emit(
        'update',
        flask.request.data,
        room=game
    )
    return "OK"


if __name__ == '__main__':
    socketio.run(app, debug=True)
