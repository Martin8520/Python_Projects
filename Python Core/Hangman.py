def get_word():
    while True:
        word = input().lower()
        if len(word) >= 4 and word.isalpha():
            return word
        else:
            print("The word is too short or has invalid characters")


def get_initial_positions(length):
    return [True] + ([False] * (length - 2)) + [True]


def hide_word(word, positions):
    return "".join([letter if tr else "-" for letter, tr in zip(word, positions)])


def check_guess(word, letter, positions):
    new_positions = [tr or (ch == letter) for ch, tr in zip(word, positions)]
    return new_positions


def check_for_win(positions):
    return all(positions)


def play_hangman():
    word = get_word()
    lives = 5
    positions = get_initial_positions(len(word))
    hidden = hide_word(word, positions)

    print(hidden)

    while True:
        next_letter = input().lower()
        new_positions = check_guess(word, next_letter, positions)

        if new_positions == positions:
            print("No such letter or already guessed")
            print(f"Lives remaining: {lives - 1}")
            lives -= 1

            if lives == 0:
                print("You lose!")
                break

        elif check_for_win(new_positions):
            print("You win!")
            break

        else:
            print("Another letter guessed!")
            hidden = hide_word(word, new_positions)
            print(hidden)

            positions = new_positions


play_hangman()
