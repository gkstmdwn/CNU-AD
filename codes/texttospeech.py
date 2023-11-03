from gtts import gTTS
import os

def tts(text:str) -> gTTS:
    audio = gTTS(text=text, lang='en', slow=False)
    return audio