import tkinter as tk
from tkinter import messagebox
import requests  # For making HTTP requests
import socketio  # For SocketIO client

app = tk.Tk()
app.title("Real-Time Chat Application")

# Initialize SocketIO client
sio = socketio.Client()

# Connect to the SocketIO server (Flask-SocketIO server)
sio.connect('http://localhost:5000')  # Adjust URL if your server is running on a different host/port

@sio.event
def connect():
    print('Connected to server')

@sio.event
def disconnect():
    print('Disconnected from server')

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    if username and password:
        response = requests.post('http://localhost:5000/login', json={'username': username, 'password': password})
        data = response.json()
        if data['success']:
            messagebox.showinfo("Login Successful", f"Logged in as {username}")
            sio.emit('join', {'username': username, 'room': 'general'})  # Join 'general' room after successful login
        else:
            messagebox.showerror("Login Failed", data['error'])
    else:
        messagebox.showerror("Error", "Username and password cannot be empty")

def join_room():
    selected_index = chat_listbox.curselection()
    if selected_index:
        room_name = chat_listbox.get(selected_index).replace(' ', '_')  # Replace spaces with underscores
        sio.emit('join', {'username': username_entry.get().strip(), 'room': room_name.lower()})  # Emit join event
        messagebox.showinfo("Room Joined", f"Joined room: {room_name}")


username_label = tk.Label(app, text="Username:")
username_label.pack()
username_entry = tk.Entry(app)
username_entry.pack()

password_label = tk.Label(app, text="Password:")
password_label.pack()
password_entry = tk.Entry(app, show="*")
password_entry.pack()

login_button = tk.Button(app, text="Login", command=login)
login_button.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=5, pady=5)

chat_label = tk.Label(app, text="Chat Rooms")
chat_label.pack()

chat_listbox = tk.Listbox(app, height=5)
chat_listbox.pack()

chat_scrollbar = tk.Scrollbar(app)
chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_listbox.config(yscrollcommand=chat_scrollbar.set)
chat_scrollbar.config(command=chat_listbox.yview)

sample_rooms = ["General", "Python Enthusiasts", "Tech Talk", "Random"]
for room in sample_rooms:
    chat_listbox.insert(tk.END, room)

join_button = tk.Button(app, text="Join Chat Room", command=join_room)
join_button.pack()

app.mainloop()
