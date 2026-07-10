import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

while True:
    text = input("Enter text: ")

    if text.lower() == "exit":
        break

    engine.say(text)
    engine.runAndWait()

    print("Finished speaking")