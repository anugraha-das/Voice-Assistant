import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
import os  

# 1. Initialize the Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    """This function makes the assistant speak out loud and prints it to the screen."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# 2. Initialize the Speech Recognition engine
recognizer = sr.Recognizer()

def listen():
    """This function listens to your microphone and converts it to text."""
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat it?")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def check_weather():
    speak("Which city's weather would you like to check?")
    city = listen()
    if city:
        try:
            url = f"https://wttr.in/{city}?format=3"
            response = requests.get(url)
            speak(response.text)
        except:
            speak("I couldn't retrieve the weather right now.")

def read_news():
    speak("Opening the latest news for you.")
    os.system("start https://news.google.com")

def set_reminder_step_by_step():
    speak("What should I remind you about?")
    reminder_text = listen()
    if reminder_text:
        save_reminder(reminder_text)

def save_reminder(text):
    speak(f"Got it. I will remind you to: {text}")
    with open("reminders.txt", "a") as file:
        file.write(f"{datetime.datetime.now()}: {text}\n")

# 3. The Main Loop controlling the assistant
def run_assistant():
    speak("Hello! I am your personal voice assistant. How can I help you today?")
    
    while True:
        command = listen()
        
        if "reminder" in command or "remind" in command:
            reminder_text = command.replace("remind me to", "").replace("set a reminder to", "").replace("remind me", "").replace("set a reminder", "").strip()
            if reminder_text == "":
                set_reminder_step_by_step()
            else:
                save_reminder(reminder_text)
            
        elif "weather" in command:
            check_weather()
            
        elif "news" in command:
            read_news()
            
        elif "time" in command:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time_now}")
            
        elif "stop" in command or "exit" in command or "bye" in command:
            speak("Goodbye! Have a great day.")
            break
        
        elif command == "":
            continue
        else:
            speak("I heard you, but I don't know that command yet.")

# Start the assistant program immediately
run_assistant()