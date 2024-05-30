MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '-..-.': '/',
    '-....-': '-', '-.--.': '(', '-.--.-': ')', '/': ' '
}


def morse_to_english(morse_code):
    words = morse_code.split('   ')
    english_translation = []

    for word in words:
        letters = word.split()
        english_word = ''.join(MORSE_CODE_DICT[letter] for letter in letters)
        english_translation.append(english_word)

    return ' '.join(english_translation)


def main():
    morse_code = input("Enter Morse Code: ")
    english_text = morse_to_english(morse_code)
    print(f"Translated Text: {english_text}")


if __name__ == "__main__":
    main()
