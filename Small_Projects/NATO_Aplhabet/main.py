import pandas

data = pandas.read_csv("_internal/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}


def gen_phonetic():
    word = input("Enter word: ").upper()
    try:
        output = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please enter a valid word.")
        gen_phonetic()
    else:
        for letter in output:
            print(letter)

    input("Press Enter to exit...")


if __name__ == "__main__":
    gen_phonetic()
