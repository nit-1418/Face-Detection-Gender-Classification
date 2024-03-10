import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os

def start_main_program():
    subprocess.Popen(["python", "main.py"])

def end_main_program():
    os.system("taskkill /f /im python.exe")

def show_about():
    messagebox.showinfo("About", "This is a simple GUI for controlling the face detection and gender classification program.")

root = tk.Tk()
root.title("Face Detection & Gender Classification")
root.geometry("600x500")
root.configure(bg="#F2F2F2")

header_label = tk.Label(root, text="Face Detection & Gender Classification", font=("Helvetica", 20, "bold"), bg="#3B5998", fg="white")
header_label.pack(pady=(20,10), fill="x")

image_path = "background.png"
image = Image.open(image_path)

image = image.resize((200, 200), Image.ANTIALIAS)

# image to Tkinter format
tk_image = ImageTk.PhotoImage(image)

# a label to display the image
image_label = tk.Label(root, image=tk_image, bg="#F2F2F2")
image_label.pack()

# Main Program Control Frame
control_frame = tk.Frame(root, bg="#F2F2F2", bd=5)
control_frame.pack(pady=20)

start_button = tk.Button(control_frame, text="Start Main Program", command=start_main_program, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
start_button.grid(row=0, column=0, padx=10)

end_button = tk.Button(control_frame, text="End Program", command=end_main_program, font=("Helvetica", 12), bg="#F44336", fg="white", padx=10, pady=5)
end_button.grid(row=0, column=1, padx=10)

about_button = tk.Button(root, text="About", command=show_about, font=("Helvetica", 12), bg="#3B5998", fg="white", padx=10, pady=5)
about_button.pack(side="bottom", pady=(10, 20))

footer_label = tk.Label(root, text="Developed by Nitesh Rajbanshi", font=("Helvetica", 13), bg="#3B5998", fg="white", padx=10, pady=5)
footer_label.pack(side="bottom", fill="x")

root.mainloop()
