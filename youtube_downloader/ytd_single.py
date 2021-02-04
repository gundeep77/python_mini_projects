import os
import string
from pytube import YouTube
from moviepy.editor import *
from pathlib import Path

if __name__ == "__main__":
    download_dir = os.path.join(Path.home(), "Desktop\\")
    link = input("\nEnter the link: ")
    try:
        vid = YouTube(link)
        my_file = vid.streams
        file_name = vid.title
        for symbol in file_name:
            if symbol in string.punctuation:
                file_name = file_name.replace(symbol, "_")
        file_name = file_name.replace(" ", "_")

        while True:
            file_type = input("Do you want to download video or only audio (Enter 'video'/'audio')? ")
            file_type = file_type.lower()
            if file_type == "video":
                print("Downloading...")
                my_file.get_highest_resolution().download(download_dir)
                print("Download Complete!")
                break
            elif file_type == "audio":
                print("Downloading...")
                file = my_file.get_audio_only().download(f"{download_dir}", filename="audio_file")
                mp3_format = AudioFileClip(file)
                mp3_format.write_audiofile(f"{download_dir}\\{file_name}.mp3")
                mp3_format.close()
                os.remove(f"{download_dir}\\audio_file.mp4")
                print("Download Complete!")
                break
            else:
                print("Please enter audio or video only!")
    except:
        print("Sorry, the link is invalid or is not available for download!")