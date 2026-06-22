<<<<<<< HEAD
# Personal Voice Assistant 🎙️🤖

A lightweight, local Python-based personal voice assistant that interacts using speech recognition and text-to-speech engine capabilities. It can fetch weather reports, launch news updates, keep track of time, and dynamically manage a custom local reminders list.

---

## 🚀 Features

* **Voice Recognition:** Powered by Google's Speech Recognition API to capture your intent cleanly.
* **Text-to-Speech:** Local audio feedback using `pyttsx3` (no internet required for speaking).
* **Smart Reminders:** Intelligent context matching. Specify the reminder inline (e.g., *"remind me to buy groceries"*) or let the assistant walk you through a step-by-step setup prompt. Reminders are saved to a local `reminders.txt` file.
* **Live Weather Checking:** Instantly pulls real-time weather statuses for any requested city.
* **Web Automation:** Quick-access handler to open up top trending global news dashboards.

---

## 🛠️ Tech Stack & Dependencies

The project uses Python along with a few highly optimized open-source libraries:

* **`speech_recognition`** - For processing microphone input.
* **`pyttsx3`** - For offline text-to-speech generation.
* **`requests`** - To hit third-party API gateways (like `wttr.in`).

---

## How to Run


Bash
python assistant.py

Available Commands:
Once the assistant is listening, you can try saying:

"Remind me to call John at 5 PM" or just "Set a reminder"

"What is the weather like?"

"Open the news"

"What time is it?"

"Stop" / "Exit" / "Goodbye"

📁 Project Layout
Plaintext
├── assistant.py          # Main execution application script
├── reminders.txt         # Auto-generated text file storing your log of tasks
└── README.md             # Project documentation
=======
# Voice-Assistant
A Python-powered offline/online local voice assistant featuring weather tracking, smart dynamic reminders, and web automation.
>>>>>>> 80a00b0abffdccb4cec6ddbd62e745f42a68087e
