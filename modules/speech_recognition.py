import speech_recognition as sr

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-US')
        print(f"User said: {command}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Can you repeat?")
        return None
    return command.lower()
