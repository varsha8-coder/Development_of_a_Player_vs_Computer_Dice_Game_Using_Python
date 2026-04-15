import random
def roll_dice():
    return random.randint(1, 6)
def play_round():
    input("Press Enter to roll the dice...")
    player = roll_dice()
    computer = roll_dice()
    print("You rolled:", player)
    print("Computer rolled:", computer)
    if player > computer:
        print("You win this round!")
        return "player"
    elif computer > player:
        print("Computer wins this round!")
        return "computer"
    else:
        print("It's a tie!")
        return "tie"
def play_game():
    rounds = int(input("Enter number of rounds: "))
    player_score = 0
    computer_score = 0
    for i in range(1, rounds + 1):
        print(f"--- Round {i} ---")
        result = play_round()

        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
    print("=== Final Scores ===")
    print("You:", player_score)
    print("Computer:", computer_score)
    if player_score > computer_score:
        print(" You are the overall winner!")
    elif computer_score > player_score:
        print(" Computer wins the game!")
    else:
        print(" The game is a tie!")
play_game()
