from email.message import EmailMessage
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pandas as pd
import psutil as pu
import smtplib  # enable less secure apps from google security settings for email feature to work


df = pd.read_excel("email_list.xlsx")
emails = {}
for i, j in df.iterrows():
    emails[j['Name'].lower()] = j['Email']


engine = pyttsx3.init()  # Microsoft Speech API, we can use the built-in voice of windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 0.6)

webbrowser.register('edge', None,
                    webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge.exe"))
edgeBrowser = webbrowser.get('edge')    # We can use chrome browser if we want, just paste the path for chrome.exe


my_name = os.environ["MY_NAME"]
my_email = os.environ["EMAIL_ADDRESS"]
my_password = os.environ["EMAIL_PASSWORD"]

def send_mail(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_email, my_password)
    server.send_message(msg)
    server.close()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning boss! What would you like me to do?")
    elif 12 <= hour < 17:
        speak("Good Afternoon boss! What would you like me to do?")
    else:
        speak("Good Evening boss! What would you like me to do?")


def takeCommand():
    # takes microphone input from user and returns out as text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 550
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")

    except Exception as e:
        return "None"

    return query


def find_process_id_by_name(process_name):
    for proc in pu.process_iter():
        if proc.name() == process_name:
            return proc.pid
    return None


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'how are you' in query:
            speak("I am fine, thank you")

        elif 'i love you' in query:
            speak("Ummm, i am not sure about that!")

        elif 'what do you do' in query:
            speak("I assist you, didn't you know?")

        elif 'tell me a joke' in query:
            speak("don't trust the atoms, they make up everything")


        elif 'tell me about' in query or 'i want to know about' in query or 'who is' in query or 'what is' in query or 'where is' in query or 'who are' in query or 'what are' in query or 'where are' in query:
            try:
                query = query.replace('tell me about', '').replace('who is', '').replace('what is', '').replace('where is', '').replace('i want to know about', '').strip()
                results = wikipedia.summary(query, sentences=2)
                speak(results)
            except Exception as e:
                print(e)
                speak("I am sorry sir, wikipedia doesn't have the requested information")


        elif 'open youtube' in query:
            speak("Opening YouTube...")
            edgeBrowser.open("youtube.com")


        elif 'open gmail' in query:
            speak("Opening Gmail...")
            edgeBrowser.open("gmail.com")


        elif 'open amazon' in query:
            speak("Opening Amazon...")
            edgeBrowser.open("amazon.in")


        elif 'open vs code' in query:
            try:
                speak("Opening VS Code...")
                path = "C:\\Users\\gssal\\AppData\\Local\\Programs\\Microsoft VS Code\\Cod.exe"
                os.startfile(path)
            except:
                speak("Sorry, there is no such application in your system")


        elif 'play music' in query or 'play some music' in query or 'play any song' in query or 'start music' in query or 'play a song' in query or 'listen to music' in query or 'play song' in query or 'play another song' in query or 'play some other song' in query or 'listen to a song' in query or 'listen to song' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            speak("Which song do you want to listen to?")
            while True:
                flag = 1
                song_name = takeCommand().lower()
                if song_name == "none":
                    continue

                if "cancel" in song_name or 'drop it' in song_name or 'leave it' in song_name or 'leave this' in song_name or "don't want to listen" in song_name:
                    speak("Okay sir, how can I help you now?")
                    break

                if 'shuffle the songs' in song_name or 'any song' in song_name or 'play any' in song_name or 'random song' in song_name:
                    os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))
                    break

                else:
                    for song in songs:
                        if song_name in song.lower():
                            flag = 0
                            os.startfile(os.path.join(music_dir, song))
                            break

                    if flag == 0:
                        break
                    elif flag == 1:
                        speak("Sorry sir, the song is not in your list")
                        continue
                

        elif 'stop the music' in query or 'stop music' in query or 'stop it' in query or 'stop this' in query or 'stop the song' in query:
            if 'Music.UI.exe' not in (p.name() for p in pu.process_iter()):
                speak("But there is no music playing sir!")
            else:
                p = pu.Process(find_process_id_by_name('Music.UI.exe'))
                p.terminate()
                continue


        elif 'send an email' in query or 'send email' in query:
            try:
                msg = EmailMessage()
                msg['From'] = my_name
                speak("Whom do you want to send to?")
                to = takeCommand().lower()
                
                if "cancel it" in to or "cancel the email" in to or 'drop it' in to or 'leave it' in to or 'leave this' in to or 'drop the plan' in to or "don't send the email" in to:
                    speak("Okay sir, how can I help you now?")
                    continue

                while to == 'none':
                    speak("Please be clear!")
                    to = takeCommand().lower()

                flag = 1
                while flag:
                    for i, j in df.iterrows():
                        if to in j['Name'].lower():
                            to = j['Email']
                            flag = 0
                            break
                    if "cancel it" in to or "cancel the email" in to or 'drop it' in to or 'leave it' in to or 'leave this' in to or 'drop the plan' in to or "don't send the email" in to:
                        speak("Okay sir, how can I help you now?")
                        break

                    if flag == 1:
                        speak("Sorry, the name is not in the list, please choose from the list")
                        to = takeCommand().lower()
                        if "cancel it" in to or "cancel the email" in to or 'drop it' in to or 'leave it' in to or 'leave this' in to or 'drop the plan' in to:
                            speak("Okay sir, how can I help you now?")
                            break
                        continue
                msg['To'] = to
                
                if flag == 0:
                    speak("What should be the subject?")
                    while True:
                        subject = takeCommand()
                        sub = subject.lower()
                        if sub == 'none':
                            speak("Are you saying something? Please be clear")
                            continue
                        temp = 0
                        if "cancel the email" in sub or 'drop it' in sub or 'leave it' in sub or 'leave this' in sub or 'drop the plan' in sub or "don't send the email" in sub:
                            speak("Okay sir, how can I help you now?")
                            temp = 1
                            break
                        else:
                            subject = subject.replace(subject[0], subject[0].upper(), 1)
                            msg['Subject'] = subject
                            break
                    if temp == 0:
                        speak("What should I say in the message?")
                        while True:
                            body = takeCommand()
                            content = body.lower()
                            if content == 'none':
                                speak("Are you saying something? Please be clear")
                                continue
                            if "cancel the email" in content or 'drop it' in content or 'leave it' in content or 'leave this' in content or 'drop the plan' in content or "don't send the email" in content:
                                speak("Okay sir, how can I help you now?")
                                break
                            else:
                                body = body.replace(body[0], body[0].upper(), 1)
                                msg.set_content(body + "\n\nGundeep")
                                send_mail(msg)
                                speak("Email has been sent!")
                                break
                

            except Exception as e:
                speak("Sorry, I am unable to send the email at the moment")


        elif 'f***' in query or 'a******' in query or 'moron' in query or 'scoundrel' in query or 'f*****' in query:
            speak("That's not polite! Learn from me")
            
        elif 'nothing' == query or 'goodbye' in query or 'good bye' in query or 'get lost' in query or 'shut it' in query or 'shut it down' in query or 'shut down' in query or 'shutdown' in query or 'bye jarvis' in query or 'see you later' in query or 'ok bye' in query or 'quit it' in query or 'close it' in query:
            speak("Goodbye sir, see you later")
            break
