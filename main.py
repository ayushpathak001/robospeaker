import pyttsx3

from gtts import gTTS
import os
language = input("Enter the robo language (H) for Hindi (E)for English : ")
if language.lower() == "H".lower():
    while True:
        text = input("Kya bolna chahte ho Robo se (exit likho band karne ke liye): ")
        if text.lower() == "exit":
            print("Robo bolta hai: Alvida Ayush!")
            tts = gTTS(text="Alvida Ayush!", lang='hi')
            tts.save("goodbye.mp3")
            os.system("start goodbye.mp3")
            break
        tts = gTTS(text=text, lang='hi')
        tts.save("voice.mp3")
        os.system("start voice.mp3")

if language.lower()== "E".lower():
    print("Welcome to RoboSpeaker 1.1 Created by Ayush")
    engine = pyttsx3.init()  # Initialize the text-to-speech engine

    while True:
        x = input("Enter what you want me to pronounce (or type 'exit' to quit): ")
        if x.lower() == "exit":
            engine.say("Goodbye Ayush!")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()