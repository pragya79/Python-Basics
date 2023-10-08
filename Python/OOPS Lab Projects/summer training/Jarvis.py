import pyttsx3 #---->text to speech
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Say Something!!")
        #removing noise from the source
        recognizer.adjust_for_ambient_noise(source)
        #listening from the source
        audio=recognizer.listen(source)
        #if we speak--->convert to text
        #if we don't--->no text
        #hence, a try and except block is needed
        try:
            print("Recognizing....")
            data=recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Not Understand")
sptext()
#upto here we have completed how to convert speech to text
#------TEXT TO SPEECH------
# def speech():
#     #syntax-->var=module.class()
#     #for speech 2 kind of voice are present male & female
#     engine = pyttsx3.init()
#     voices=