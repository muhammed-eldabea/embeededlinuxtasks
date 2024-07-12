import gtts as gt
import os
import time
import speech_recognition as sr
import simpleaudio as sa
from pydub import AudioSegment  # Import AudioSegment from pydub

def speak(text):
    tts = gt.gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)

    # Convert MP3 to WAV using pydub
    sound = AudioSegment.from_mp3(filename)
    sound.export("voice.wav", format="wav")

    # Play the WAV file
    wave_obj = sa.WaveObject.from_wave_file("voice.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

    os.remove(filename)  # Remove the original MP3
    os.remove("voice.wav")  # Remove the temporary WAV file

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

if __name__ == "__main__":
    speak("Hello, I am Mekanos, your smart assistant. How can I help you?")
    while True:
        text = listen()
        if "Mekanos" in text:
            text = text.replace("Mekanos", "")
            if "exit" in text:
                speak("Goodbye!")
                break
            else:
                speak(f"You said: {text}")
                # Add your logic here to process the user's request
                # For example, you can use if-else statements to handle different commands
                # ...
        if "time" in text:
            speak("The current time is " + time.strftime("%H:%M:%S"))
            
        if "date" in text:
            speak("The current date is " + time.strftime("%d/%m/%Y"))
            
        if "hello" in text:
            speak("Hello there!")
            
        if "how are you" in text:
            speak("I am doing well, thank you for asking.")
        if "exit" in text:
            speak("Goodbye!")
            break     
        time.sleep(1)