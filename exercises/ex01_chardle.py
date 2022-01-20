"""EX01 - Chardle - A cute step toward Wordle."""

_author_ = "730234932"

word_choice: str = input("Enter a 5-character word: ")

if len(word_choice) != 5:
    print("Error: Word must contain 5 characters")
    quit()

character_choice: str = input("Enter a single character: ")

if len(character_choice) != 1:
    print("Error: Character must be a single character.")
    quit()

print("Searching for " + character_choice + " in " + word_choice)

instances: int = 0

if character_choice == word_choice[0]:
    print(character_choice + " found at index 0")
    instances = instances + 1

if character_choice == word_choice[1]:
    print(character_choice + " found at index 1")
    instances = instances + 1

if character_choice == word_choice[2]:
    print(character_choice + " found at index 2")
    instances = instances + 1

if character_choice == word_choice[3]:
    print(character_choice + " found at index 3")
    instances = instances + 1
     
if character_choice == word_choice[4]:
    print(character_choice +" found at index 4")
    instances = instances + 1

if instances == 0:
    print("No instances of " + character_choice + " found in " + word_choice)
else:
    if instances == 1:
        print(str(instances) + " instance of " + character_choice + " found in " + word_choice)
    else:
        print(str(instances) + " instances of " + character_choice + " found in " + word_choice)


