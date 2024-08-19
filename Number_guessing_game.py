import random
random_number=random.randint(1, 10)
guess=0
while(guess!=random_number):
    guess=int(input("Enter a number : "))
    if(guess<random_number):
        print("Try again! Too low...")
    elif(guess>random_number):
        print("Try again! Too high...")
print(f"Congrats! you guessed the number {guess}")