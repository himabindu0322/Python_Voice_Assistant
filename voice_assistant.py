import speech_recognition as sr
import pyttsx3
import webbrowser
import os

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()


def speak(text):
    """Convert text to speech"""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to user's voice and return command"""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return ""

        except sr.RequestError:
            speak("Please check your internet connection.")
            return ""


# Assistant starts
speak("I'm ready to do your work. Tell me what should I do for you.")

while True:
    command = listen()

    if command:
        # Repeat what the user said
        speak(command)

        # Open YouTube
        if "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # Open Google
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        # Open Gmail
        elif "open gmail" in command:
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com")

        # Open WhatsApp Web
        elif "open whatsapp" in command:
            speak("Opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com")

        # Open Calculator
        elif "open calculator" in command:
            speak("Opening Calculator")
            os.system("calc")

        # Open Notepad
        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        # Open Paint
        elif "open paint" in command:
            speak("Opening Paint")
            os.system("mspaint")

        # Open File Explorer
        elif "open file explorer" in command:
            speak("Opening File Explorer")
            os.system("explorer")

        # Open Command Prompt
        elif "open command prompt" in command:
            speak("Opening Command Prompt")
            os.system("start cmd")

        # Exit Assistant
        elif "stop" in command or "exit" in command:
            speak("Okay, Goodbye.")
            break

        # Unknown command
        else:
            speak("Sorry, I don't know how to do that yet.")
