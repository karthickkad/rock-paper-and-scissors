import random
#Initialize of you_score and computer_score.
you_score = 0
computer_score = 0

def get_user_choice(): #function to get userchoice.
    """
    Function to get user's choice (rock, paper, or scissors)
    """
    while True: #continue loop until the game ends
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():#computers_choice
    """
    Function to randomly generate computer's choice
    """
    return random.choice(['rock', 'paper', 'scissors']) #random generator of words

def determine_winner(user_choice, computer_choice): #comparing user_choice and computer_choice to determine the winner 
    """
    Function to determine the winner of the game
    """
    global you_score, computer_score; #global declaration 
#determine winner in each round
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
         
        you_score = you_score + 1
        return "Congratulations! You win this round!"
    else:
        computer_score = computer_score + 1
        return "Computer wins this round!"


"""
Function to play the game
"""
print("Let's play Rock, Paper, Scissors!")
print("\n")
n = int(input("How many rounds do you want to play? "))
count = 1 
#loop for no.of.rounds played based on user input
while n > 0:
    print(f"Round: {count}")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))
    count = count + 1
    n = n - 1
#determine overall winner.
if you_score > computer_score:
    print("You won the overall match")
elif you_score < computer_score:
    print("Computer won the overall match")
else:
    print("The match is tied")
