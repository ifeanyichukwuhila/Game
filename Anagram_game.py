import random

words = ["mango", "pineapple", "kiwi", "attend", "bread"]


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
        guess = input("Enter your guess: ").strip().lower()

        if guess == word:
            points = len(word)
          #  score += points
            score = score + points
            print("Correct! You earned", points, "points.")
        else:
            #lives -= 1
            lives = lives - 1
            print("Wrong guess! The correct word was:", word)
            print("Lives remaining:", lives)

    print("\n===== GAME OVER =====")
    print("Final score:", score)


play_game()
