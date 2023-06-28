import random


def play_game():
    print("Welcome to My HANG-MAN Game!!!")

    words = ["banana", "apple", "cable", "tree", "cap", "shark"]

    random_word = random.choice(words)

    # print(random_word)
    # guess = input("Guess a word:")
    # print(random_word)

    # This is to check if the word guessed is in the list.
    # for letter in random_word:
    #     if letter == guess:
    #         print("Right")
    #     else:
    #         print("Wrong")
    #         break

    # Generate Blanks
    # for word in words:
    #     blanks = ["_" * len(words)]
    game_over = False
    lives = 6
    guessed_letters = []  # THIS IS A VARIABLE I MADE TO STOP THE REPETITION OF DISPLAY
    display = []
    word_length = len(random_word)
    for _ in range(word_length):
        display += "_"

    # guess = input("Guess a letter from the list:").lower()

    # for position in range(word_length):
    #     letter = random_word[position]
    #
    #     if letter == guess:
    #         display[position] = letter

    # THE TRIAL IF-STATEMENT ALLOWS THE USER INPUT TO TAKE BOTH UPPER-CASE AND LOWER-CASE!!!
    # if guess.lower() == guess:
    #     print(display)
    #
    # elif guess.upper() == guess:
    #     print(display)
    #
    # else:
    #     print("Invalid guess.")
    while "_" in display:
        guess = input("Guess a random letter:").lower()

        # START OF THE CODE TO END THE REPETITION

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        letters_found = False

        # END OF THE CODE

        for position in range(word_length):
            letter = random_word[position]

            # print(display)

            if letter == guess:
                display[position] = letter
                letters_found = True  # LAST PART OF THE CODE

        print(display)
        if not letters_found:
            print("You are wrong")
            lives -= 1
            print("You have", lives, "left")

            # print(display)
            if lives == 0:
                game_over = True
                print("Game over! You ran out of lives.")
                break  # TO BREAK OUT OF THE WHILE LOOP
    if not game_over:
        print("Congratulations! You guessed the word:", random_word)

        # print(display)

        # if letter != guess:
        #     # display[position] = letter
        #     print("You are wrong! please guess again ")
        #     # display[position] = letter
        # else:
        #     display[position] = letter
        #     print(display)
        #
        # if "_" in display:
        #     print("You are correct guess again!")
    # print("Congratulations! You guessed the word:", random_word)

    # print(display)

    # while "_" in display:
    #     guess = input("Guess a letter from the list:").lower()

    # print(display)

    # print(display)

    # blanks = ["_" * len(word) for word in words]
    # print(blanks)


while True:
    play_game()
    play_again = input("DO YOU WANT TO PLAY AGAIN? (yes/no):").lower()
    if play_again == "yes":
        # play_game()
        continue
    else:
        print("THANK YOU FOR PLAYING! GOODBYE...")
        break
