# 🤖 AURIX - AI Assistant

AURIX is a Jarvis-like AI assistant built using Python with voice interaction, system control, and intelligent automation.

---

## 🚀 Features

- 🎤 Voice + Text Interaction  
- 🧠 Smart Wake Word Detection (Aurix, RX, Alex, etc.)  
- ⚙️ System Control (Open apps, take screenshots)  
- 🔄 Task Automation (Study Mode, Coding Mode)  
- 🤖 AI Conversation using Local LLM (Ollama)  
- 📊 System Awareness (Battery, CPU usage)  
- 🛡️ Capability Guard (Prevents unsafe actions)  
- 📁 Logging System (aurix.log)  
- ⚡ Graceful Error Handling  

---

## 🧱 Architecture

Input → Wake Word → Intent Detection → Capability Guard → Execution (System / AI)

---

## 🛠️ Tech Stack

- Python  
- SpeechRecognition  
- pyttsx3  
- psutil  
- pyautogui  
- Ollama (LLM)  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py