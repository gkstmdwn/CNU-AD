from gtts import gTTS
import os

def tts(text:str) -> gTTS:
    audio = gTTS(text=text, lang='en', slow=False)
    return audio

if __name__ == "__main__":
    tts("Hello sir, my name is SeungJoo").save('tts.wav')