# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# recognizer=sr.Recognizer()
# engine=pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# if __name__== "__main__":
#     speak("Initializing AI Assisstant")
#     while True:
#         r=sr.Recognizer()
#         with sr.Microphone() as source:

#             print("Listening...")
#             audio=r.listen(source)

#             try:
#                 command= r.recognize_sphinx(audio)
#                 print(command)
#             except OSError as e:
#                 print(f"Microphone error: {e}")
#                 exit()
#             except sr.UnknownValueError:
#                 print("Sphinx could not understand audio")
#             except sr.RequestError as e:
#                 print("Sphinx error; {0}".format(e))

import speech_recognition as sr
import pyttsx3
import webbrowser
import mp3Lib
from gtts import gTTS
import pygame
from openai import OpenAI
import os
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def mp3Play(mp3File):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3File)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_new(text):
    tts = gTTS(text)
    tts.save('test.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load("test.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("test.mp3")

def aiAns(command):
    client = OpenAI(
   
    )
    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {"role":"system","content":"You are a virtual Assistant named Siri"},
            {"role": "user", "content": command}
        ]
    )
    print(completion.choices[0].message)

def processCommand(instructions):
    print(instructions)
    if "open linkedin" in instructions.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open facebook" in instructions.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open instagram" in instructions.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open google" in instructions.lower():
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in instructions.lower():
        webbrowser.open("https://www.youtube.com/")
    elif instructions.lower().startswith("play"):
        song = instructions.lower().split(" ")[1]
        link=mp3Lib.music[song]
        print(link)
        webbrowser.open(link)
    else:
        speak_new(aiAns(instructions))
        
if __name__ == "__main__":
    speak("Initializing AI Assistant")
    while True:
        r = sr.Recognizer()
        print("Siri started!")
        try:
            with sr.Microphone(sample_rate=16000) as source:  # Setting a lower sample rate
                print("Listening...")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            if(word.lower()=="siri"):
                speak("Yes, how can i help you!")
                with sr.Microphone(sample_rate=16000) as source:  # Setting a lower sample rate
                    print("Siri is Listening")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print(f"You are getting an error: {e}")

