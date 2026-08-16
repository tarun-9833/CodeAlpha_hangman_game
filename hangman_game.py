import random

words = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]

word = random.choice(words)
guessed_word = ["_"] * len(word)

wrong_guesses = 0
max_wrong_guesses = 6
guessed_letters = []

print("================================")
print("       HANGMAN GAME")
print("================================")

while wrong_guesses < max_wrong_guesses and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if "_" not in guessed_word:
    print("\nCongratulations! 🎉")
    print("You guessed the day:", word)
else:
    print("\nGame Over!")
    print("The correct day was:", word)