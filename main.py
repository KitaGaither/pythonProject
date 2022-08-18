import datetime
import pytz
import pywhatkit
import speech_recognition as sr
import pyttsx3
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                print(command)
    except:
        pass
    return command

def run_alex():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)
    elif 'hello' in command:
        print('Hello, how are you?')
        speak('Hello, how are you?')
    elif 'what is your name' in command:
        print('My name is alex, what is your name?')
        speak('My name is alex, what is your name?')
    elif 'time' in command:
        time = datetime.datetime.now(pytz.timezone('US/Central')).strftime('%I:%M %p')
        print('The current time is ' + time + ' central standard time')
        speak('The current time is ' + time + ' central standard time')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(pyjokes.get_joke())
    elif 'goodbye' in command:
        print('Goodbye')
        speak("Goodbye")
        greeting_end = exit(0)
        greeting_end
    else:
        speak('Please say the command again')

while True:
    run_alex()




