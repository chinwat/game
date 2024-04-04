import random

class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed_letters = set()
        self.remaining_guesses = 6

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        return displayed_word

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            print("You already guessed that letter!")
            return
        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.remaining_guesses -= 1

    def is_game_over(self):
        if self.remaining_guesses <= 0:
            return True, "You lose! The word was '{}'.".format(self.word)
        elif "_" not in self.display_word():
            return True, "Congratulations! You guessed the word '{}'.".format(self.word)
        else:
            return False, None


def main():
    words = ["monday", "hangman", "silpakorn", "computer", "keyboard", "game","ECS","code"]
    word = random.choice(words)
    game = Hangman(word)

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while not game.is_game_over()[0]:
        print("\nWord:", game.display_word())
        print("Remaining guesses:", game.remaining_guesses)

        guess = input("Enter a letter: ")
        game.guess(guess)

    print(game.is_game_over()[1])


if __name__ == "__main__":
    main()

