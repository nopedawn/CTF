import paramiko
import io
import tkinter as tk
from tkinter import messagebox

hostname = "137.184.250.54"
port = 7031
username = "mack"
private_key = """
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
"""


ascii_arts = [
    """
    blabla
    """
]

def get_remote_time():
    try:
        key = paramiko.RSAKey.from_private_key(io.StringIO(private_key))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, pkey=key)
        stdin, stdout, stderr = ssh.exec_command("date")
        time = stdout.read().decode().strip()
        ssh.close()
        return time
    except Exception as e:
        messagebox.showerror("Connection Error", f"Failed to fetch time: {str(e)}")
        return "Error"

def refresh_time():
    time = get_remote_time()
    time_label.config(text=time)

def cycle_ascii_art(index=0):
    art_label.config(text=ascii_arts[index])
    next_index = (index + 1) % len(ascii_arts)
    root.after(100, cycle_ascii_art, next_index)

def create_gui():
    global root, art_label, time_label
    root = tk.Tk()
    root.title("itsabouttime")
    root.configure(background='black')

    window_width = 650
    window_height = 700
    root.geometry(f"{window_width}x{window_height}")

    title_label = tk.Label(root, text="""
.__  __              _____ ___.                  __    ___________.__
|__|/  |_  ______   /  _  \\_ |__   ____  __ ___/  |_  \__    ___/|__| _____   ____
|  \   __\/  ___/  /  /_\  \| __ \ /  _ \|  |  \   __\   |    |   |  |/     \_/ __ \
|  ||  |  \___ \  /    |    \ \_\ (  <_> )  |  /|  |     |    |   |  |  Y Y  \  ___/
|__||__| /____  > \____|__  /___  /\____/|____/ |__|     |____|   |__|__|_|  /\___  >
              \/          \/    \/                                         \/     \/
        """, font=("Courier", 8), justify=tk.LEFT, background="black", foreground="green")
    title_label.pack(pady=10)

    art_label = tk.Label(root, text=ascii_arts[0], font=("Courier", 4), justify=tk.CENTER, background="black", foreground="green")
    art_label.pack()

    time_label = tk.Label(root, text="Fetching time...", font=("Helvetica", 14), background="black", foreground="green")
    time_label.pack(pady=10)

    refresh_button = tk.Button(root, text="Refresh Time", command=refresh_time, background="black", foreground="green")
    refresh_button.pack(pady=10)

    # Start cycling ASCII art
    root.after(1, cycle_ascii_art)

    # Fetch initial time
    refresh_time()

    root.mainloop()


if __name__ == "__main__":
    create_gui()
