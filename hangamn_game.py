# hang man game
import random
chars=["apple","grape","lemon","table","chair"]
num1=random.choice(chars)
print(num1)

print("Hnageman game ")
print("Word: _ _ _ _ _")
print("Attempt :6")
attempt=6
guess1=[]
while True:
    guess=str(input("Guessed a letter: "))
    attempt-=1
    if guess in num1:
        print(f"Good guess! \n Attempt left :{attempt} \n  ")
        guess1.append(guess)
        num2="".join(guess1)
    elif guess not in num1:
        print(f"wrong guess! \n Attempt left {attempt}")
    if attempt==0:
        print("Thanks you")
        break
    if num2==num1:
        print("congrats you win!")
        break
              


