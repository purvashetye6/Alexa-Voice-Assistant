import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)

def alexa_talk(text):
    engine.say(text)
    engine.runAndWait()


def alexa_listen():
    try:
        with sr.Microphone() as source:
            listener.energy_threshold = 10000
            listener.adjust_for_ambient_noise(source, 1.2)

            print('listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '')

    except:
        pass    

    return command

def run_alexa():
    command = alexa_listen()

    if 'play' in command:
        command = command.replace('play', '')
        alexa_talk('Playing' + command)
        pywhatkit.playonyt(command)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        alexa_talk('The current time is' + time)

    elif 'information' in command:
        command = command.replace('Get me information about', '')
        alexa_talk('Getting information.' + command)
        information = wikipedia.summary(command, 4)
        print(information)
        alexa_talk(information)

    elif 'joke' in command:
        alexa_talk('Here is a joke')
        joke = pyjokes.get_joke()
        print(joke)
        alexa_talk(joke)

    else:
        alexa_talk('Could you please repeat it again')

alexa_talk('Hello. I am Alexa. What can I do for you?')        

while True:
    run_alexa()