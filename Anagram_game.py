
import random


def load_words():
    with open("words_alpha.txt", "r", encoding="utf-8") as file:
        words = file.read().splitlines()

    words = [
        word.strip().lower()
        for word in words
        if word.strip().isalpha()
        and 4 <= len(word.strip()) <= 8
    ]

    if not words:
        raise ValueError("The dictionary contains no valid words.")

    return words


def scramble_word(word):
    scrambled = word

    while scrambled == word:
        letters = list(word)
        random.shuffle(letters)
        scrambled = "".join(letters)

    return scrambled


def play_game():
    score = 0
    lives = 3

    print("===== ANAGRAM GAME =====")
    print("Unscramble the letters to find the word!")
    print("You have 3 lives.")

    while lives > 0:
        word = random.choice(words)
        scrambled = scramble_word(word)

        print("\nScrambled word:", scrambled)

        while True:
            guess = input("Enter your guess (or type 'hint'): ").strip().lower()

            if guess == "hint":
                print("Hint: The word starts with the letter '" + word[0].upper() + "'")

            elif len(guess) != len(word):
                print("Your guess must contain", len(word), "letters. Try again.")

            else:
                break

        if guess == word:
            points = len(word)
            score = score + points
            print("Correct! You earned", points, "points.")

        else:
            lives = lives - 1
            print("Wrong guess! The correct word was:", word)
            print("Lives remaining:", lives)

    print("\n===== GAME OVER =====")
    print("Final score:", score)


try:
    words = load_words()
    play_game()

except (FileNotFoundError, ValueError) as error:
    print("Something went wrong:", error)
