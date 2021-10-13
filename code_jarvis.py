pip install SpeechRecognition
pip install pyttsx3
pip install --upgrade pip
# SPEECH TO TEXT RECOGNITION

import speech_recognition

jarvis = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Listening...\n")
    audioCapture = jarvis.listen(source)

    recognizeText = jarvis.recognize_google(audioCapture)
    print(recognizeText)

# pip install pipwin
# pipwin install pyaudio
import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()

speak("Hello Palak! how are you???")

# MY OWN JARVIS 
import speech_recognition
import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()

jarvis = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Listening...\n")
    audioCapture = jarvis.listen(source)

    recognizeText = jarvis.recognize_google(audioCapture)
    print(recognizeText)
    speak(recognizeText)

	# MY OWN JARVIS 
import speech_recognition
import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()

jarvis = speech_recognition.Recognizer()

condition = True
while condition:
    with speech_recognition.Microphone() as source:
        print("Listening...\n")
        audioCapture = jarvis.listen(source)

        try:
            recognizeText = jarvis.recognize_google(audioCapture)

            if 'exit' in recognizeText:
                condition = False

            else:
                print(recognizeText)
                speak("Hello how are you")
            
        except:
            print("Please repeat")
