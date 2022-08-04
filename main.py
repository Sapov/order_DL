import shutil
import os
from pathlib import Path
p = Path.home()
target_path = str(p) + '\\Downloads'

files_downloads = os.listdir(target_path)
dir_name = ['PDF', 'Programs', 'Picturies', 'Docs', 'Arhivs', "Corel_makets", 'Video']
for i in range(len(dir_name)):  # проверяем ессть ли каталог нет создаем
    if not os.path.exists(target_path + '\\' + dir_name[i]):
        os.mkdir(target_path + '\\' + dir_name[i])  # Создаем папкИ


for i in range(len(files_downloads)-1):
    # print(files_downloads[i])

    if files_downloads[i][-3:] == 'jpg' or files_downloads[i][-3:] == 'png':
        print(files_downloads[i], "This's JPG")
        shutil.move(target_path + "\\" + files_downloads[i], target_path + "\\" + 'Picturies')
        print(target_path + "\\" + files_downloads[i])
    elif files_downloads[i][-3:] == 'pdf':
        print(files_downloads[i], "This's PDF")
        shutil.move(target_path + "\\" + files_downloads[i], target_path + "\\" + 'PDF')
    elif files_downloads[i][-4:] == 'docx' or files_downloads[i][-3:] == 'xlsx':
        print(files_downloads[i], "This's DOC")
        shutil.move(target_path + "\\" + files_downloads[i], target_path + "\\" + 'Docs')
    elif files_downloads[i][-3:] == 'zip' or files_downloads[i][-3:] == 'rar':
        print(files_downloads[i], "This's ARH")
        shutil.move(target_path + "\\" + files_downloads[i], target_path + "\\" + 'Arhivs')
    elif files_downloads[i][-3:] == 'exe' or files_downloads[i][-3:] == 'msi' or files_downloads[i][-3:] == 'apk':
        print(files_downloads[i], "This's Proga")
        shutil.move(target_path + "\\" + files_downloads[i], target_path + "\\" + 'Programs')
    elif files_downloads[i][-3:] == 'cdr':
        print(files_downloads[i], "This's COREL files")
        shutil.move(target_path + "\\" + files_downloads[i], target_path + "\\" + 'Corel_makets')
    elif files_downloads[i][-3:] == 'avi' or files_downloads[i][-3:] == 'mkv':
        print(files_downloads[i], "<== This's Video files")
        shutil.move(target_path + "\\" + files_downloads[i], target_path + "\\" + 'Video')
    elif files_downloads[i][-7:] == 'torrent':
        print(files_downloads[i], "<== This's Trash")
        # shutil.move(target_path + "\\" + files_downloads[i], target_path + "\\" + 'Video')
        os.remove(os.path.join(target_path + "\\", files_downloads[i]))
