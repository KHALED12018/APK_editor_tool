import os
import tkinter as tk
from tkinter import filedialog
import subprocess
import platform

root = tk.Tk()
root.title(" apk_editor by Dragn-Noir2023")

# Function to select the APK file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("APK files", "*.apk")])
    apk_path.set(file_path)

# Function to extract the APK
def extract_apk():
    apk_file = apk_path.get()
    if apk_file:
        output_folder = os.path.dirname(apk_file)
        command = "apktool d " + apk_file + " -o " + output_folder
        if platform.system() == "Windows":
            subprocess.run(command, shell=True)
        else:
            subprocess.run(command.split())

# Function to build the APK
def build_apk():
    apk_folder = os.path.dirname(apk_path.get())
    command = "apktool b " + apk_folder
    if platform.system() == "Windows":
        subprocess.run(command, shell=True)
    else:
        subprocess.run(command.split())

# GUI elements
apk_path = tk.StringVar()
tk.Label(root, text="  apk (APK):").pack()
tk.Entry(root, textvariable=apk_path).pack()
tk.Button(root, text=" chose", command=select_file).pack()

tk.Button(root, text="unpack ", command=extract_apk).pack()
tk.Button(root, text="Repack  ", command=build_apk).pack()

# Treeview to display extracted files
tree_frame = tk.Frame(root)
tree_frame.pack()
tree_scroll = tk.Scrollbar(tree_frame)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

tree = tk.Listbox(tree_frame, yscrollcommand=tree_scroll.set)
tree.pack(side=tk.LEFT, fill=tk.BOTH)
tree_scroll.config(command=tree.yview)

root.mainloop()
