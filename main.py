import ollama
import datetime
import speech_recognition as sr
import pyttsx3
import platform
import psutil
import os
import subprocess
import pyautogui
import logging

# ================= CONFIG =================
DEBUG_MODE = True

# ================= LOGGING =================
logging.basicConfig(
    filename="aurix.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(message):
    logging.info(message)

# ================= SYSTEM PROMPT =================
SYSTEM_PROMPT = """
You are AURIX, a reliable AI assistant.
If unsure, ask for clarification.
Never hallucinate system capabilities.
"""

conversation = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# ================= WAKE WORD =================
WAKE_WORD_VARIANTS = ["aurix", "orix", "orex", "rx", "alex", "erix", "forex"]
FILLER_WORDS = ["hey", "hi", "hello", "play", "please"]

# ================= SPEECH =================
engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 175)

def speak(text):
    try:
        engine.stop()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        log_event(f"TTS error: {str(e)}")

# ================= VOICE INPUT =================
def listen_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You (voice):", text)
        return text.lower()
    except sr.UnknownValueError:
        log_event("Voice not understood")
        return ""
    except Exception as e:
        log_event(f"Voice error: {str(e)}")
        return ""

# ================= WAKE WORD LOGIC =================
def clean_input(text):
    for word in FILLER_WORDS:
        text = text.replace(word, "")
    return text.strip()

def wake_word_detected(text):
    cleaned = clean_input(text)
    return any(v in cleaned for v in WAKE_WORD_VARIANTS)

# ================= SAFE SYSTEM ACTIONS =================
def open_app(app):
    apps = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "notepad": "notepad.exe",
        "vscode": r"C:\Users\HP\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    }

    if app in apps:
        try:
            if os.path.exists(apps[app]) or app == "notepad":
                os.startfile(apps[app])
                log_event(f"Application opened: {app}")
                return f"Opening {app}."
            else:
                log_event(f"App path missing: {app}")
                return f"I cannot find {app} on this system."
        except Exception as e:
            log_event(f"Error opening {app}: {str(e)}")
            return f"Something went wrong while opening {app}."
    else:
        return "That application is not allowed."

def take_screenshot():
    try:
        file = f"screenshot_{datetime.datetime.now().strftime('%H%M%S')}.png"
        pyautogui.screenshot(file)
        log_event(f"Screenshot taken: {file}")
        return "Screenshot taken."
    except Exception as e:
        log_event(f"Screenshot error: {str(e)}")
        return "I couldn't take a screenshot."

# ================= SYSTEM INFO =================
def get_battery_status():
    try:
        b = psutil.sensors_battery()
        if b:
            log_event("Battery checked")
            return f"Battery is at {b.percent}%."
        return "Battery information not available."
    except Exception as e:
        log_event(f"Battery error: {str(e)}")
        return "I couldn't check battery status."

def get_cpu_usage():
    try:
        usage = psutil.cpu_percent(interval=1)
        log_event("CPU usage checked")
        return f"CPU usage is {usage}%."
    except Exception as e:
        log_event(f"CPU error: {str(e)}")
        return "I couldn't check CPU usage."

# ================= MAIN LOOP =================
print("AURIX running — Stage 6 Part 2: Graceful Recovery\n")

while True:
    thoughts = []

    mode = input("Press Enter to type, or 'v' for voice: ")

    if mode.lower() == "v":
        user_input = listen_voice()
        thoughts.append("Voice input")
    else:
        user_input = input("You: ").lower()
        thoughts.append("Text input")

    if not user_input:
        speak("I didn't catch that.")
        continue

    log_event(f"User input: {user_input}")

    if user_input == "exit":
        speak("Goodbye.")
        log_event("AURIX terminated.")
        break

    if not wake_word_detected(user_input):
        if DEBUG_MODE:
            print("🧠 Thoughts: Wake word not detected")
        continue

    response = None

    # -------- COMMAND ROUTING --------
    if "study" in user_input:
        log_event("Automation: Study mode triggered")
        open_app("chrome")
        response = "Study mode activated."

    elif "open chrome" in user_input:
        response = open_app("chrome")

    elif "screenshot" in user_input:
        response = take_screenshot()

    elif "battery" in user_input:
        response = get_battery_status()

    elif "cpu" in user_input:
        response = get_cpu_usage()

    else:
        try:
            ai = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": user_input}]
            )
            response = ai["message"]["content"]
            log_event("AI response generated")
        except Exception as e:
            log_event(f"AI failure: {str(e)}")
            response = "I'm having trouble connecting to my AI engine."

    print("AURIX:", response)
    speak(response)
