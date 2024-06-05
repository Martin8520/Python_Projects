import pyttsx3


def initialize_tts():
    """Initialize the TTS engine and list available voices."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    print("Available voices:")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name} ({voice.id})")

    return engine, voices


def set_voice(engine, voices, voice_index):
    """Set the TTS engine to use the specified voice."""
    engine.setProperty('voice', voices[voice_index].id)


def text_to_speech(engine, text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()


def display_menu():
    """Display the menu and get the user's choice."""
    print("\nChoose an option:")
    print("1. Enter text to convert to speech")
    print("2. Change voice")
    print("3. Exit")
    return input("Enter your choice: ")


def main():
    engine, voices = initialize_tts()

    while True:
        choice = display_menu()

        if choice == '1':
            text = input("Enter the text: ")
            text_to_speech(engine, text)
        elif choice == '2':
            voice_index = int(input("Enter the voice index you want to use: "))
            if 0 <= voice_index < len(voices):
                set_voice(engine, voices, voice_index)
                print(f"Voice changed to {voices[voice_index].name}")
            else:
                print("Invalid voice index. Please try again.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
