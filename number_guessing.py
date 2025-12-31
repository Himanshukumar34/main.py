import random
import_random=random.randint(1,100)


while True:
    user_input=int(input("Enter your num:"))
    if user_input==import_random:
        print("🎉you guess right num,congrats",import_random)
        break
    elif user_input>import_random:
        print("your nunber is high,try again")
    elif user_input<import_random:
        print("your guess is low,try again")
   



