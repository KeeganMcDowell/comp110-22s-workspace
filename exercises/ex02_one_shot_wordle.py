"""EX02 - One shot wordle."""

__author__ = "730234932"

secret_word: str = str("hello")
guessed_word: str = input(f"What is your {len(secret_word)}-letter guess? ") 

while len(guessed_word) != len(secret_word):
    guessed_word = input(f"That was not {len(secret_word)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

idx: int = 0
guess_results: str = ""

while idx < len(guessed_word):
    if guessed_word[idx] == secret_word[idx]:
        guess_results = f"{guess_results}{GREEN_BOX}"
    else:   
        letter_used: bool = False
        aidx: int = 0
        while letter_used is not True and aidx < len(secret_word):
            if guessed_word[idx] == secret_word[aidx]:
                letter_used = True
            else:
                aidx = aidx + 1
        if letter_used is True:
            guess_results = f"{guess_results}{YELLOW_BOX}"
        else: 
            guess_results = f"{guess_results}{WHITE_BOX}"
    idx = idx + 1

print(guess_results)

if guessed_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")