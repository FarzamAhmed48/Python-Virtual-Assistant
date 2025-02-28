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
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

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

