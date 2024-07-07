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
    while True:
        text = listen()  # Comment out this line
        if text:
            speak(text)  # Comment out this line
        time.sleep(1)