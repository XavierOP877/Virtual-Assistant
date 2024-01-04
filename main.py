import os

def speak(text):
    voice = "en-US-ArialNeural"
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'
    os.system(command)
speak("hello I am your virtual assistant how may i help you!")