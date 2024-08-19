import random
def play(user,computer):
    if(user==computer):
        return "Its a Tie"
    elif(user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r') :
       return "Congrats! You won..." 
    else:
        return "You lost !! Better luck next time..."
   
def get_user_choice():
    while True:
        user_choice = input('Enter your choice [Rock -> r, Paper -> p, Scissors -> s]: ').strip().lower()
        if user_choice in ['r', 'p', 's']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'r', 'p', or 's'")


user_choice = get_user_choice()
computer_choice =random.choice(['r','p','s'])
result=play(user_choice,computer_choice)
print(f"Computer choice : {computer_choice}\n {result}")

