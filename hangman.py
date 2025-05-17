import random


word_list = ['python', 'developer', 'hangman', 'keyboard', 'function', 'variable''doctor',
              'engineer', 'teacher', 'firefighter', 'pilot','galaxy', 'planet','umbrella', 'mountain', 'library', 'puzzle']


chosen_word = random.choice(word_list)
word_length = len(chosen_word)


max_attempts = 6
attempts = 0
guessed_letters = []
display = ['_'] * word_length

print(" Welcome to Hangman!")
print("You have", max_attempts, "incorrect guesses allowed.")
print("Word to guess: ", " ".join(display))

while attempts < max_attempts and '_' in display:
    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print(" Correct!")
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        print(" Incorrect!")
        attempts += 1

    print("Word: ", " ".join(display))
    print("Wrong guesses left:", max_attempts - attempts)

# Game result
if '_' not in display:
    print("\n Congratulations! You guessed the word:", chosen_word)
else:
    print("\n Game Over! The word was:", chosen_word)
    print("\n Better Luck next time")

