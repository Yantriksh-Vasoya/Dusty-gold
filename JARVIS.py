import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, there was an error with the speech recognition: {e}")
        return ""


def voice_assistant():
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "what is your name" in command:
            speak("I am jarvis.")
        elif "How are you ?" in command:
            speak("I am fine. what about you sir?..how was your day")
        elif 'wikipedia' in command:
            speak('searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in command:
            webbrowser.open("youtube.com")
        elif 'open google' in command:
            webbrowser.open("google.com")
        elif 'open instagram' in command:
            webbrowser.open("instagram.com")
        elif "goodbye" in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    voice_assistant()
