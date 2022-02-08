"""EX03 - The actual wordle."""

__author__ = "730234932"


def contains_char(secret_word: str, letter_check: str) -> bool:
    """Checking a guessed letter against each index of the secret word."""
    assert len(letter_check) == 1
    idx: int = 0
    letter_used: bool = False
    while idx < len(secret_word):
        if secret_word[idx] == letter_check:
            letter_used = True 
        idx = idx + 1
    return letter_used  


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guessed_word: str, secret_word: str) -> str:
    """Returns a set of boxes representing whether the word matches the letters in a guessed word."""
    assert len(guessed_word) == len(secret_word)
    guess_results: str = ""
    idx_guess: int = 0
    while idx_guess < len(secret_word):
        if guessed_word[idx_guess] == secret_word[idx_guess]:
            guess_results = f"{guess_results}{GREEN_BOX}"
        else:
            if contains_char(secret_word, guessed_word[idx_guess]) is True:
                guess_results = f"{guess_results}{YELLOW_BOX}" 
            else:
                guess_results = f"{guess_results}{WHITE_BOX}"
        idx_guess = idx_guess + 1
    return guess_results


def input_guess(expected_length: int):
    """Ensuring an inputed word is the correct length."""
    guessed_word: str = input(f"Enter a {expected_length} character word: ")
    while len(guessed_word) != expected_length:
        guessed_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return guessed_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 1
    max_turns: int = 6
    wordle_word: str = "codes"
    won: bool = False
    while turn_number <= max_turns and won is False:
        print(f"=== Turn {turn_number}/{max_turns} ===")
        guessed_word: str = input_guess(len(wordle_word))
        print(emojified(guessed_word, wordle_word))
        if guessed_word == wordle_word:
            won = True
            print(f"You won in {turn_number}/{max_turns} turns!")
        else:
            turn_number = turn_number + 1
    if won is False:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()