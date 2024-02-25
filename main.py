import json
import shutil
import tkinter as tk
import tkinter.filedialog
import zipfile
import os

import requests

program_path = os.getcwd()


def download_mods(mod_data):
    os.makedirs(os.path.join('files', 'overrides', 'mods'), exist_ok=True)

    for mod in mod_data:
        download_url = mod['downloads'][0]

        os.path.basename(mod['path'])
        output_path = os.path.join(program_path, 'file', 'overrides', mod['path'])

        response = requests.get(download_url)

        with open(output_path, 'wb') as f:
            f.write(response.content)


def create_mods_folder():
    overrides_path = os.path.join(program_path, 'file', "overrides")
    mods_path = os.path.join(overrides_path, "mods")
    if not os.path.exists(mods_path):
        os.makedirs(mods_path)

    with open(os.path.join(program_path, 'file', 'modrinth.index.json')) as file:
        file_data = json.load(file)
        download_mods(file_data['files'])


def copy_and_unzip(file_path):
    source_path = file_path
    destination_path = os.path.join(program_path, "file.mrpack")
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    shutil.copyfile(source_path, destination_path)

    with zipfile.ZipFile(destination_path, "r") as zip_file:
        zip_file.extractall(os.path.join(program_path, "file"))

    create_mods_folder()


def choose_file(event):
    print('sus')
    filename = tk.filedialog.askopenfilename(filetypes=[("MRPack files", "*.mrpack")])
    if filename:
        pass
        #copy_and_unzip(filename)


root = tk.Tk()
root.title("MRPack Extractor")
#button_choose = tk.Button(root, text="Выбрать файл", command=choose_file)

#button_choose.grid(row=0, column=2)
drop_frame = tk.Frame(root, bg='green', width=50, height=10)
drop_frame.pack(padx=5, pady=5)

drop_frame.bind('<<Drop>>', choose_file)


root.mainloop()
