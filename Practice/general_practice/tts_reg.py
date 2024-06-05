import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

print("Available Voices:")
for i, voice in enumerate(voices):
    print(f"{i+1}. {voice.name}")

selected_index = int(input("Enter the index of the voice you want to use: ")) - 1

if 0 <= selected_index < len(voices):
    selected_voice = voices[selected_index]

    engine.setProperty('voice', selected_voice.id)

    # Say something
    engine.say("Hello, I'm speaking using the selected voice.")

    # Wait for speech to finish
    engine.runAndWait()
else:
    print("Invalid voice index. Please select a valid index.")
