import pyttsx3
import tkinter as tk

# Initialize the TTS engine
engine = pyttsx3.init()

# Get all available voices
voices = engine.getProperty('voices')

# Function to speak with selected voice
def speak_with_selected_voice():
    selected_index = voice_listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        selected_voice = voices[selected_index]
        engine.setProperty('voice', selected_voice.id)
        text_to_speak = text_entry.get()
        engine.say(text_to_speak)
        engine.runAndWait()
    else:
        status_label.config(text="Please select a voice.")

# Create GUI
root = tk.Tk()
root.title("Voice Selection")

# Create listbox to display available voices
voice_listbox = tk.Listbox(root, width=40)
for voice in voices:
    voice_listbox.insert(tk.END, voice.name)
voice_listbox.pack(padx=10, pady=5)

# Create input box for text
text_entry = tk.Entry(root, width=50)
text_entry.pack(padx=10, pady=5)

# Create button to speak with selected voice
speak_button = tk.Button(root, text="Speak", command=speak_with_selected_voice)
speak_button.pack(pady=5)

# Create label to display status
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
