word_to_guess = input("Enter the word to guess: ").lower()
word_length = len(word_to_guess)
score = 10

if word_length <= 3:
    print("Word is too short.")
else:
    guessed_word = word_to_guess[0] + "_" * (word_length - 2) + word_to_guess[-1]

    correct_guesses = set()

    while "_" in guessed_word:
        print("Current word:", guessed_word)
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha() and guess.islower():
            if guess in correct_guesses:
                print("You've already guessed this letter correctly. Try again.")
            else:
                guessed = False
                for i in range(1, word_length - 1):
                    if word_to_guess[i] == guess:
                        guessed_word = guessed_word[:i] + guess + guessed_word[i+1:]
                        correct_guesses.add(guess)
                        guessed = True
                if not guessed:
                    score -= 1
                    print(f"Incorrect guess. Your score is now {score}. Try again.")
        else:
            print("Please enter a single lowercase letter.")

    print(f"You guessed the word '{word_to_guess}' with a score of {score}")
