import random

words = ["apple", "grape", "lemon", "table", "chair"]
secret_word = random.choice(words)

attempts = 6
guessed_letters = []

print("---- Hangman Game ----")

while attempts > 0:
    # display word
    display_word = ""
    for ch in secret_word:
        if ch in guessed_letters:
            display_word += ch + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ")

    if len(guess) != 1:
        print("❌ Please guess only ONE letter\n")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed this letter\n")
        continue

    if guess in secret_word:
        print("✅ Good guess!\n")
        guessed_letters.append(guess)
    else:
        print("❌ Wrong guess!\n")
        attempts -= 1

    # win condition
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You won!")
        break

if attempts == 0:
    print("😢 You lost! The word was:", secret_word)


              


