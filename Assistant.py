import speech_recognition as sr
import datetime
import pyttsx3
import webbrowser
import os 
import wikipedia


engine=pyttsx3.init()
engine.setProperty("rate",170)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
recognizer=sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis sir please tell me how can i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
       print("Recognizing..")
       query = r.recognize_google(audio,language="en-in")
       print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please..")
        return "None"
    return query.lower()


def main():
    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")    
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")  
            speak("Opening google")  

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

    
        elif 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Sorry, I didn't understand that.")


if __name__ == "__main__":
    main()
