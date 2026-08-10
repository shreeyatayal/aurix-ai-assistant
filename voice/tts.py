import pyttsx3

# ================= SPEECH =================
engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 175)

def speak(text):
    try:
        print("DEBUG: Entered speak()")

        engine.say(text)

        print("DEBUG: Before runAndWait()")

        engine.runAndWait()

        print("DEBUG: Finished speaking")

    except Exception as e:
        print("TTS ERROR:", e)