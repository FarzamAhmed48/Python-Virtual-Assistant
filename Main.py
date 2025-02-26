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

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing AI Assistant")
    while True:
        r = sr.Recognizer()
        print("Siri started!")
        try:
            with sr.Microphone(sample_rate=16000) as source:  # Setting a lower sample rate
                print("Listening...")
                audio = r.listen(source)
                # if(audio.lower()=="siri"):
                #     speak("Yes, how can i help you!")
                #     with sr.Microphone(sample_rate=16000) as source:  # Setting a lower sample rate
                #         print("Listening...")
                #         audio = r.listen(source,timeout=2)
                try:
                    word = r.recognize_google(audio)
                    audio = r.listen(source)
                    if(word.lower()=="siri"):
                        speak("Yes, how can i help you!")
                        with sr.Microphone(sample_rate=16000) as source:  # Setting a lower sample rate
                            print("Siri is Listening")
                            audio = r.listen(source)
                            command = r.recognize_google(audio)
                            print(command)
                except sr.UnknownValueError:
                    print("Sphinx could not understand audio")
                except sr.RequestError as e:
                    print(f"Sphinx error: {e}")
        
        except OSError as e:
            print(f"Microphone error: {e}")
            break  # Exit the loop if there's a mic issue

