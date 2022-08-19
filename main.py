"""
Author: Kita G.

I created a virtual assistant.
This virtual assistant uses python's text to speech and
Google's speech recognition engine to listen and respond to users.
I created this application because my son loves
interacting with virtual assistants such as siri, alexa and cortana.
I thought it would be cool for me to create
something similar for him.
"""

# imported packages
import datetime
import sys
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
    """speak function: here the engine listens to voice commands from the user
    and then waits for a response and then responds accordingly.
    """
    engine.say(text)
    engine.runAndWait()

def take_command():
    """take_command function: The virtual assistant is listening for a
    command. She will try to execute the command and if she cannot,
    she will execute the error code.
    """
    try:
        with sr.Microphone() as source:
            print('I am listening...')
            voice = listener.listen(source)
            voice.pause_threshold = 0.5
            command = listener.recognize_google(voice)
            command = command.lower()
            print('Your command: ' + command)
    except UnboundLocalError as uerr:
        print("Handling error:", uerr)
    return command


def run_alex():
    """run_alex function: This is the core of my application. These are the commands
    that I taught to my virtual assistant.
    """
    command = take_command()
    if 'hello' in command:
        speak('Hello, how are you?')
    elif 'how are you' in command:
        print("I'm living the dream")
        speak("I'm living the dream")
    elif 'what is your name' in command:
        print('My name is alex, what is your name?')
        speak('My name is alex, what is your name?')
    elif 'kita' in command:
        print("It's nice to meet you kita")
        speak("It's nice to meet you kita")
    elif 'time' in command:
        time = datetime.datetime.now(pytz.timezone('US/Central')).strftime('%I:%M %p')
        print('The current time is ' + time + ' central standard time')
        speak('The current time is ' + time + ' central standard time')
    elif 'play' in command:
        song = command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    elif 'great job' in command:
        praise = 'Thank you, I try my best.'
        print(praise)
        speak(praise)
    elif 'goodbye' in command:
        print('Goodbye')
        speak("Goodbye")
        sys.exit()
    else:
        print("Sorry, I haven't been taught how to respond to that.")
        speak("Sorry, I haven't been taught how to respond to that.")

# while loop: Keeps alex on and listening for commands.
while True:
    run_alex()
