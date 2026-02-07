import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
recognizer=sr.Recognizer()
engine= pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open chrome" in c.lower():
        webbrowser.open("https://chrome.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif "open YouTube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startwith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)

if __name__=="__main__":
    speak("Hey, akanksha")
    while True:
        recognizer = sr.Recognizer()
        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening... Speak now!")
                audio = recognizer.listen(source)               
            word=recognizer.recognize_google(audio)
            if(word.lower()=="alexa"):
                speak("ya")
                with sr.Microphone() as source:
                    print("Alexa Listening... Speak now!")
                    audio = recognizer.listen(source)
                    command=recognizer.recognize_google(audio)

                    processCommand(command)
               
            text = recognizer.recognize_google(audio)
            print("You said:", text)
        except Exception as e:
            print("Could not understand".format(e))

