paper = "Paper"
scissor = "Scissors"

player_move = input("Choose [r]ock, [p]aper or [s]cissors:")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissor
else:
    raise SystemExit ("Invalid Input. Try again...")

computer_random_number = random.randint(1, 3)
computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissor

if (player_move == rock and computer_move == scissor) or (player_move == paper and computer_move == rock) or \
        (player_move == scissor and computer_move == paper):
    print("You win")
elif (player_move == paper and computer_move == scissor ) or (player_move == scissor and computer_move == rock) or \
        (player_move == rock and computer_move == paper):
    print("You lose")
else:
    print("Draw!")
