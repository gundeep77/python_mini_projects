import os
import shutil

folders = {"Images": ['.png', '.jpeg', '.jpg', '.ico'], "Music": ['.mp3', '.wav', '.m4a'], "Videos": ['.mp4', '.avi', '.mkv', '.wmv', '.flv'], "Archives": ['.rar', '.zip', '.iso', '.tar'], "PDF Files": ['.pdf'], "Python Files": ['.py', '.pyw', '.ipynb', '.pyc'], "Applications": ['.exe', '.app'], "Documents": ['.doc', '.docx'], "Spreadsheets": ['.xls', '.xlsx', '.xlsm'], "Text Files": ['.txt'], "Java Files": ['.class', '.java'], "C++ Files": ['.c', '.cpp'], "Shortcuts": ['.lnk']}

extensions = {}
for folder,ext_list in folders.items():
    for ext in ext_list:
        extensions[ext] = folder

cwd = os.getcwd()

for file in os.listdir(cwd):
    if os.path.isfile(file):
        ext = os.path.splitext(file)[1]
        if ext in extensions:
            if not os.path.exists(f".\\{extensions[ext]}"):
                os.mkdir(f".\\{extensions[ext]}")
                shutil.move(file, f".\\{extensions[ext]}")
            else:
                shutil.move(file, f".\\{extensions[ext]}")
        else:
            if not os.path.exists(".\\Others"):
                os.mkdir(".\\Others")
                shutil.move(file, ".\\Others")
            else:
                shutil.move(file, ".\\Others")