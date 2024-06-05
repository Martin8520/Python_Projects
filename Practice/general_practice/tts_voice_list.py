import win32com.client


def list_available_voices():
    """List available voices using SAPI5."""
    try:
        sapi5 = win32com.client.Dispatch("SAPI.SpVoice")
        voices = sapi5.GetVoices()
        print("Available voices:")
        for index, voice in enumerate(voices):
            print(f"{index}: {voice.GetDescription()} ({voice.Id})")
    except Exception as e:
        print("Error occurred while listing voices:", e)


if __name__ == "__main__":
    list_available_voices()
