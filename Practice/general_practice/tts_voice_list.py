import pyttsx3


def list_available_voices(engine):
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name} ({voice.id})")


engine = pyttsx3.init()
list_available_voices(engine)
