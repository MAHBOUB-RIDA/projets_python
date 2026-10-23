import random
print("🎲 Welcome to the number gussing Game ")

# 1 ... 10 : 1 2 8 10

secret_number = random.randint(1,10) # 4
attemp = 0
while True :
    guess = input("Enter a number between 1 and 10 : ") # 3
    guess = int(guess)
    attemp += 1
    
    # guess == secret_number
        #correct
        
    if guess == secret_number:
        print(f"🎉 Correct You guessed the number in {attemp} tries")
        break
    
    # guess > secret_number
        # too high
        
    elif guess > secret_number:
        print("🔼 Too high ! try again")
      
    # guess < secret_number
        # too low
        
    else:
        print("🔽 Too low ! try again")