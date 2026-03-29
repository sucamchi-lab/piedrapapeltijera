import random

# Initialize scores
user_score = 0
computer_score = 0

while True:
    # Get user input
    user_input = input(
        "Enter your choice (rock, paper, scissors) or 'quit' to exit: ")

    # Check if user wants to quit
    if user_input.lower() == 'quit':
        break

    # Generate computer choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # Determine the winner
    if user_input.lower() == computer_choice.lower():
        print("It's a tie!")
    elif (user_input.lower() == 'rock' and computer_choice.lower() == 'scissors') or \
         (user_input.lower() == 'paper' and computer_choice.lower() == 'rock') or \
         (user_input.lower() == 'scissors' and computer_choice.lower() == 'paper'):
        user_score += 1
        print("computer chose:", computer_choice)
        print("You win!")
    elif (user_input.lower() == 'rock' and computer_choice.lower() == 'paper') or \
         (user_input.lower() == 'paper' and computer_choice.lower() == 'scissors') or \
         (user_input.lower() == 'scissors' and computer_choice.lower() == 'rock'):
        computer_score += 1
        print("computer chose:", computer_choice)
        print("Computer wins!")
    else:
        print("Invalid input. Please try again.")

    # Print scores
    print(f"User: {user_score} Computer: {computer_score}")
