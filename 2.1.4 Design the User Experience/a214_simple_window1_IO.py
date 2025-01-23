#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.title("Authorization")
root.wm_geometry("200x200")

frame_login = tk.Frame(root)
frame_login.grid()
lbl_username = tk.Label(frame_login, text="Username", font="Courier")
lbl_username.pack()
password = tk.Label(frame_login, text="Password", font="Courier")
password.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
root.mainloop()