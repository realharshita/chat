import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("Real-Time Chat Application")

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    if username and password:
        messagebox.showinfo("Login Successful", f"Logged in as {username}")
    else:
        messagebox.showerror("Error", "Username and password cannot be empty")

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

join_button = tk.Button(app, text="Join Chat Room")
join_button.pack()

app.mainloop()
