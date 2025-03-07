import random
playing = True

number = random.randint(0,20)

print("I will guess a number from 0 to 20, you have to guess it one digit at a time")
print("The game ends when the number is guessed\n\n")

while playing:
    
    guess = int(input("Enter your guess: "))
    
    if guess < number :
        print("Your guess Numer is LESSER than the Correct Number")
    
    elif guess > number:
        print("Your guess Number Is Higher Than the Correct Number")
        
        
    elif number == guess:
        print("Your Guess is correct!")
        print(f"The number was {number}")
        break