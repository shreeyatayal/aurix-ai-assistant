import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

engine.say("Hello. This is a test of Aurix voice output.")
engine.runAndWait()
