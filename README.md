# Python_Voice_Assistant
A Python-based voice assistant that listens to voice commands and opens websites or applications using speech recognition and text-to-speech technology.

# 🎙️ Voice Assistant using Python

A simple Python-based voice assistant that listens to your voice commands and opens websites or applications on your computer using Speech Recognition and Text-to-Speech technology.

## 🚀 Features

* Converts text to speech
* Listens to voice commands using your microphone
* Opens websites like YouTube, Google, Gmail, and WhatsApp Web
* Opens Windows applications such as Calculator, Notepad, Paint, File Explorer, and Command Prompt
* Continuously listens for commands until you say **"Stop"** or **"Exit"**
* Provides voice feedback for every command

## 🛠️ Technologies Used

* Python
* SpeechRecognition
* pyttsx3
* PyAudio
* Webbrowser
* OS Module

## 📂 Project Structure

```
Voice-Assistant/
│
├── voice_assistant.py
└── requirements.txt
```

## 📦 Installation

Clone the repository:

```bash
git clone <repository-url>
cd Voice-Assistant
```

Install the required dependencies:

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

If PyAudio installation fails on Windows:

```bash
pip install pipwin
pipwin install pyaudio
```

## ▶️ Run the Project

```bash
python voice_assistant.py
```

## 🗣️ Example Commands

* Open YouTube
* Open Google
* Open WhatsApp
* Open Calculator
* Open Notepad
* Open Paint
* Open File Explorer
* Open Command Prompt
* Stop
* Exit

## 💡 Example Workflow

Assistant: I'm ready to do your work. Tell me what should I do for you?

You: Open YouTube

Assistant: Open YouTube

Assistant: Opening YouTube

➡️ YouTube opens automatically in your browser.

## 🎯 Future Enhancements

* Open any installed application dynamically
* Search queries directly on Google
* Play songs on YouTube
* Tell date and time
* Weather updates
* AI-powered chatbot integration

## Author
Karri Himabindu
