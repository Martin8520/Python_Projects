import pyttsx3


engine = pyttsx3.init()

voices = engine.getProperty('voices')

print("Available Windows Narrator Voices:")
for voice in voices:
    if "narrator" in voice.name.lower():
        print("Name:", voice.name)
        print("ID:", voice.id)
        print()
