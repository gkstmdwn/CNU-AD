import speech_recognition

def s2t(audiofile:str) -> str:
    r = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(audiofile) as source:
        audio = r.record(source)
    return r.recognize_google(audio, language='en')

if __name__ == "__main__":
    print(s2t("tts.wav"))