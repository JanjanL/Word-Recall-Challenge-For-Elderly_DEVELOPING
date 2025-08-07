'''A simple word memorization game with progressive hints.

This game challenges players to recall a missing word from a displayed list.
It offers multiple attempts and provides helpful hints to guide the player.

1.  **Game Flow:**
    *   Three words are initially shown, followed by a 5-second countdown.
    *   After the countdown, one word will be hidden, and the player is encouraged to memorize and identify it.
    *   Several attempts are allowed for guessing the missing word.

2.  **Hint System:**
    *   Hints are provided when an attempt is incorrect (based on `word_dict` values).
    *   On the **2nd attempt**, descriptive clues are given.
        *   *Example:* If the `correct_answer` is "laptop" and the 2nd attempt is "labol", hints like "It's a machine, cold and square" might be given, followed by a partial word hint like `la____`.
    *   Subsequent incorrect alphabetic guesses will also reveal more letters in the partial word hint.

3.  **Input Validation:**
    *   User input is checked to ensure it contains only alphabetic characters.
    *   No integers or symbols are allowed.
    *   All valid input is converted to lowercase for comparison.
'''

import random
import time
import os
random.seed(8)
import pandas

word_dict = {"laptop": ["machine", "contain a screen", "cold"],  
            "apple": ["delicious", "healthy", "red"],       
            "hongkong": ["city", "skyscrapers", "harbor"],
            }
word_key = list(word_dict.keys())
questions = word_key.copy()
random_selection = random.randint(0, len(word_key)-1)
answer = word_key[random_selection]
hints = "_" * len(answer)
attempts = 3

def clear_terminal():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(a):
    """
    Countdown into every second and print out the second remain
    """
    for i in range(a):
        print(a-i)
        time.sleep(1)

#Game started

print(f"Welcome! Try to remember these words: {word_key}")
countdown(5)
clear_terminal()
questions[random_selection] = hints # Hide the selected word in the list
print(f"There is a word missing: {questions}")

for i in range(attempts):
    if i ==1:
        user_input = input(f"Attempt{i+1}: Any idea? " \
                            f"It is {word_dict[answer][0]}, {word_dict[answer][1]} "\
                            f"and {word_dict[answer][2]}, the missing word will be: ")
        print()
    else:
        user_input = input(f"Attempt{i+1}: Any idea? the missing word is: ")
        print()

    # Word Processing: check if it alphabet and lower case
    if user_input.isalpha():

        # Answer Correctly
        if user_input and user_input.lower() != answer:
            user_input = user_input.lower()

            # Remove Duplicate 
            input_p = ""
            for i in user_input: #e.g. abell -> abel
                if i not in input_p:
                    input_p += i

            # Answer Checking
            for i, j in enumerate(answer): #e.g. 0, l from laptop
                hints = list(hints)
                if hints[i] == "_" and j in input_p:
                    hints[i] = j
            hints = "".join(hints) #e.g. hints ="la____"
            
            if i == 2 :
                print(f"Hi there, the answer is: {answer}. Good try")
            else:
                print(f"Good try, you are closer. What is your answer: {hints}")

        else:
            print("Congratulation, well done!")
            break

    # Input Other Than Alphabet
    else: 
        if i == 2:
            print(f"Hi there, the answer is: {answer}. Good try!")
        else:
            print(f"Hi there, alphabet only. Try again")
    
    