from modules.speech_recognition import take_command
from modules.text_to_speech import speak
from modules.system_control import shutdown, sleep
from modules.google_search import search_google
from modules.wikipedia_search import search_wikipedia

def main():
    while True:
        command = take_command()

        if command:
            if 'shutdown' in command:
                speak("Shutting down the system")
                shutdown()
                break

            elif 'sleep' in command:
                speak("Putting the system to sleep")
                sleep()
                break

            elif 'search google for' in command:
                query = command.replace('search google for', '')
                search_google(query)

            elif 'what is' in command:
                query = command.replace('what is', '')
                result = search_wikipedia(query)
                speak(result)

if __name__ == "__main__":
    main()
# xauth list > /tmp/.Xauthority && XAUTHORITY=/tmp/.Xauthority python3 assistant.py && rm /tmp/.Xauthority