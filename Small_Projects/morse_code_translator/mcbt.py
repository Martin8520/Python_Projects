import tkinter as tk
from tkinter import ttk

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def english_to_morse(text):
    return ' '.join(MORSE_CODE_DICT[char] for char in text.upper() if char in MORSE_CODE_DICT)


def morse_to_english(morse_code):
    words = morse_code.split('   ')
    english_translation = []

    for word in words:
        letters = word.split()
        english_word = ''.join(REVERSE_MORSE_CODE_DICT[letter] for letter in letters)
        english_translation.append(english_word)

    return ' '.join(english_translation)


def english_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)


def binary_to_english(binary):
    binary_values = binary.split()
    ascii_characters = [chr(int(b, 2)) for b in binary_values]
    return ''.join(ascii_characters)


def translate():
    input_text = input_text_box.get("1.0", tk.END).strip()
    if mode.get() == 'English to Morse':
        translated_text = english_to_morse(input_text)
    elif mode.get() == 'Morse to English':
        translated_text = morse_to_english(input_text)
    elif mode.get() == 'English to Binary':
        translated_text = english_to_binary(input_text)
    elif mode.get() == 'Binary to English':
        translated_text = binary_to_english(input_text)
    else:
        translated_text = "Invalid mode selected."

    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, translated_text)


def clear_text():
    input_text_box.delete("1.0", tk.END)
    output_text_box.delete("1.0", tk.END)


root = tk.Tk()
root.title("Code Translator")
root.geometry("600x450")

title_label = ttk.Label(root, text="Code Translator", font=("Helvetica", 16))
title_label.pack(pady=10)

mode = tk.StringVar(value='English to Morse')
english_to_morse_rb = ttk.Radiobutton(root, text='English to Morse', variable=mode, value='English to Morse')
morse_to_english_rb = ttk.Radiobutton(root, text='Morse to English', variable=mode, value='Morse to English')
english_to_binary_rb = ttk.Radiobutton(root, text='English to Binary', variable=mode, value='English to Binary')
binary_to_english_rb = ttk.Radiobutton(root, text='Binary to English', variable=mode, value='Binary to English')

english_to_morse_rb.pack()
morse_to_english_rb.pack()
english_to_binary_rb.pack()
binary_to_english_rb.pack()

input_label = ttk.Label(root, text="Input Text")
input_label.pack(pady=5)
input_text_box = tk.Text(root, height=5, width=60)
input_text_box.pack(pady=5)

translate_button = ttk.Button(root, text="Translate", command=translate)
translate_button.pack(pady=5)

output_label = ttk.Label(root, text="Output Text")
output_label.pack(pady=5)
output_text_box = tk.Text(root, height=5, width=60)
output_text_box.pack(pady=5)

clear_button = ttk.Button(root, text="Clear", command=clear_text)
clear_button.pack(pady=5)

root.mainloop()
