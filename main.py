import random
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")

    possible_actions = ['rock', 'paper', 'scissors']

    computer_action = random.choice(possible_actions)

    if user_action == computer_action:
        print(f"You both selected {user_action} . It's a tie!!")
    elif user_action == 'rock':
        if computer_action == 'paper':
            print("paper covers rock... You lose!!")
        else:
            print("rock smashes scissors... You win!!")
    elif user_action == 'paper':
        if computer_action == 'rock':
            print("paper covers rock... You win!!")
        else:
            print("scissors cut paper... You lose!!")
    elif user_action == 'scissors':
        if computer_action == 'paper':
            print("scissors cut paper... You win!!")
        else:
            print("rock smashes scissors... You lose!!")

    play_again = input("Do you want to play again?? (y/n): ")
    if play_again != 'y':
        break
