from Small_Projects.caesar_art import logo

print(logo)
play = True
while play:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(text_plain, shift_amount):
        cipher_txt = ""
        for ch in text_plain:
            pos = alphabet.index(ch)
            if direction == "encode":
                new_pos = (pos + shift_amount) % 26
                new_ch = alphabet[new_pos]
                cipher_txt += new_ch
            elif direction == "decode":
                new_pos = (pos - shift_amount) % 26
                new_ch = alphabet[new_pos]
                cipher_txt += new_ch
        print(f"The encoded text is {cipher_txt}")


    caesar(text_plain=text, shift_amount=shift)

    again = input("Do you want to restart the cipher? 'y'/'n': ")
    if again == "y":
        play = True
    else:
        play = False
