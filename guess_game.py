import random

def guess_game(filepath):
    try:
        with open(filepath, 'r') as f:
            word_bank = [line.strip() for line in f if line.strip()]
        
        if not word_bank:
            print("File is empty.")
            return
        
        secret_word = random.choice(word_bank).lower()
        display = [' _ '] * len(secret_word)
        total_guesses = len(secret_word)
        revealed = set()
        wrong_attempts = 0

        print(f"\nThe word you need to guess has {len(secret_word)} characters")
        print(f"You have now {total_guesses} guesses")

        while ' _ ' in display and wrong_attempts < total_guesses:
            print('\n' + ''.join(display))
            user_input = input("\nGuess a character: ").lower()

            if not (len(user_input) == 1 and user_input.isalpha()):
                print("Please enter a single alphabetical character.")
                continue

            correct_guess = False
            for pos, letter in enumerate(secret_word):
                if letter == user_input and pos not in revealed:
                    display[pos] = f" {user_input} "
                    revealed.add(pos)
                    correct_guess = True
                    break

            if not correct_guess:
                print("Sorry, that letter is not in the word.")
                wrong_attempts += 1
                print('\n' + ''.join(display))

            if ' _ ' in display:
                print(f"\nYou have {total_guesses - wrong_attempts} guess(es) left\n")
                print('-' * 30)

        if ' _ ' not in display:
            print(f'\nYou found the word --> "{secret_word}"')
            print("Congratulations! You won!")
        else:
            print("\nSorry! You lost!")
            print(f'The word was --> "{secret_word}"')

    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
        return []

if __name__ == "__main__":
    guess_game("words.txt")
