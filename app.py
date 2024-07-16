from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

users = {
    'user1': {'password': 'pass1'},
    'user2': {'password': 'pass2'}
}

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username in users and users[username]['password'] == password:
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Invalid credentials'})

if __name__ == '__main__':
    socketio.run(app)
