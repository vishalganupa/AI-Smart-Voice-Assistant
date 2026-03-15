from google import genai
from apikey import api_data
import speech_recognition as sr
import pyttsx3
import webbrowser

# Gemini model
MODEL = "gemini-2.0-flash"

client = genai.Client(api_key=api_data)


def Reply(question):
    response = client.models.generate_content(
        model=MODEL,
        contents=question
    )

    return response.text


# Text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Hello. How can I help you?")


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)

    except Exception:
        print("Say that again...")
        return "none"

    return query


if __name__ == "__main__":

    while True:

        query = takeCommand().lower()

        if query == "none":
            continue

        if "bye" in query:
            speak("Goodbye")
            break

        if "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")
            continue

        if "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")
            continue

        ans = Reply(query)

        print(ans)

        speak(ans)