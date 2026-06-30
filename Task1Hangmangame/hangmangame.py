import random

words = ["python", "coding", "laptop", "internship", "developer"]

word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display = ""

   
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    
    if "_" not in display:
        print(" Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print(" Wrong guess!")
        print("Remaining attempts:", attempts)
    else:
        print("✅ Correct guess!")


if attempts == 0:
    print("\n Game Over!")
    print("The word was:", word)