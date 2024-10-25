import speech_recognition as sr

def take_command():
    r = sr.Recognizer()
    
    # Chỉ định thiết bị âm thanh cụ thể (ví dụ: pulse hoặc default)
    mic = sr.Microphone(device_index=8)  # Thử với index 8 (pulse) hoặc 12 (default)

    with mic as source:
        print("\n==>Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        print("\n==>Recognizing...")
        command = r.recognize_google(audio)
        print(f"\n==>Command: {command}")
        return command
    except sr.UnknownValueError:
        print("\n==>Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("\n==>Could not request results; check your network connection.")
        return None