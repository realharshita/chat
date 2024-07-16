from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Dictionary to store chat rooms and their participants
chat_rooms = {
    'general': [],
    'random': [],
    'python_enthusiasts': []
}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('join')
def join(data):
    username = data['username']
    room = data['room'].replace(' ', '_').lower()  # Replace spaces with underscores and convert to lowercase
    print(f'Received room name: {room}')  # Print the received room name for debugging
    if room in chat_rooms:
        join_room(room)
        chat_rooms[room].append(username)
        emit('update_users', {'users': chat_rooms[room]}, room=room)
        print(f'{username} joined room: {room}')
    else:
        print(f'Room "{room}" does not exist')

if __name__ == '__main__':
    socketio.run(app)
