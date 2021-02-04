import os
import pkg_resources

required = ["pytube", "moviepy", "plyer"]
installed = []
for pkg in list(pkg_resources.working_set):
    installed.append(str(pkg).split()[0])

for pkg in required:
    if pkg not in installed:
        os.system(f"pip install {pkg}")

import string
from pytube import YouTube
from moviepy.editor import *
from pathlib import Path
from plyer import notification as nt


def download_video(link):
    vid = YouTube(link)
    my_file = vid.streams
    my_file.get_highest_resolution().download(f"{download_dir}\\Videos")

def download_audio(link):
    vid = YouTube(link)
    file_name = vid.title
    for symbol in file_name:
        if symbol in string.punctuation:
            file_name = file_name.replace(symbol, "_")
    file_name = file_name.replace(" ", "_")
    file = YouTube(link).streams.get_audio_only().download(f"{download_dir}\\Audios", filename="audio_file")
    mp3_format = AudioFileClip(file)
    mp3_format.write_audiofile(f"{download_dir}\\Audios\\{file_name}.mp3")
    mp3_format.close()
    os.remove(f"{download_dir}\\Audios\\audio_file.mp4")

def driver_code():
    flag = 0
    youtube_links_file_path = os.path.join(Path.home(), "Desktop", "Enter links here.txt")
    if not os.path.exists(youtube_links_file_path):
        f_temp = open(youtube_links_file_path, 'w')
        f_temp.close()
        nt.notify(
            title = "YouTube Downloader",
            message = 'A temporary file named "Enter links here" has been created. Please enter the links in the correct format, save it and run the application again!',
            timeout = 15,
            app_icon = rf"{os.getcwd()}\youtube.ico"
        )
        return
        
    f = open(youtube_links_file_path, 'r')
    file = f.readlines()
    
    if not len(file):
        nt.notify(
            title = "YouTube Downloader",
            message = '''"Enter links here" file can't be empty!''',
            timeout = 5,
            app_icon = rf"{os.getcwd()}\youtube.ico"
        )
        return

    nt.notify(
            title = "YouTube Downloader",
            message = 'Download Started!\nYou will be notified when it completes.',
            timeout = 5,
            app_icon = rf"{os.getcwd()}\youtube.ico"
        )    

    invalid_links = []
    for i,line in enumerate(file):
        if line == "\n":
            continue

        if len(line.split()) != 2:
            flag = 2
            if os.path.exists(unsuccessful_logs_file):
                with open(unsuccessful_logs_file, "a+") as f1:
                    f1.write(
                        f"Incorrect format used to enter the link and file-type (only audio or video accepted) at line number {i+1} in the temporary links file!\n\n"
                )
            else:
                os.mkdir(download_dir)
                with open(unsuccessful_logs_file, "w") as f1:
                    f1.write(
                        f"Incorrect format used to enter the link and file-type (only audio or video accepted) at line number {i+1} in the temporary links file!\n\n"
                )
            continue
    
        link = line.split()[0].strip().strip('\n')
        file_type = line.split()[1].strip().strip('\n').lower()

        try:
            yt = YouTube(link)
        except:
            invalid_links.append((link, i+1))
            continue

        if file_type == 'audio':
            download_audio(link)
        elif file_type == 'video':
            download_video(link)
        else:
            flag = 1
            if os.path.exists(unsuccessful_logs_file):
                with open(unsuccessful_logs_file, "a+") as f2:
                    f2.write(
                        f"Incorrect format used to enter the link and file-type (only audio or video accepted) at line number {i+1} in the temporary links file!\n\n"
                )
            else:
                os.mkdir(download_dir)
                with open(unsuccessful_logs_file, "w") as f2:
                    f2.write(
                        f"Incorrect format used to enter the link and file-type (only audio or video accepted) at line number {i+1} in the temporary links file!\n\n"
                )
            continue

    if len(invalid_links) or flag == 1 or flag == 2:
        nt.notify(
            title = "YouTube Downloader",
            message = "Some links could not be downloaded, please see the log file in the YouTube Downloads folder.",
            timeout = 15,
            app_icon = rf"{os.getcwd()}\youtube.ico"
        )
        
        for link in invalid_links:
            with open(unsuccessful_logs_file, "a+") as f1:
                f1.write(
                    f"Invalid link {link[0]} at line number {link[1]} in the text file containing links!\n\n"
            )
        f.close()
    else:
        nt.notify(
            title = "YouTube Downloader",
            message = "Downloading Finished!\nThanks for using the YouTube Downloader!",
            timeout = 15,
            app_icon = rf"{os.getcwd()}\youtube.ico"
        )
        f.close()
        os.remove(os.path.join(Path.home(), "Desktop", "Enter links here.txt"))


if __name__ == "__main__":
    download_dir = os.path.join(Path.home(), "Desktop", "YouTube Downloads(Python)\\")
    unsuccessful_logs_file = download_dir + "unsuccessful_downloads_logs.txt"
    driver_code()