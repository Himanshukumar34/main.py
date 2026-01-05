# number guessing game with exceptional handling
import  random
num1=random.randint(1,100);
count=0
while  True:
    try :
        guess=int(input("Enter your guess :"))
        count+=1
        if guess==num1:
            print("congrats you win , your total attempt ",count)
            break
        elif guess>num1:
            print("your guess is greator , try again")
        elif guess<num1:
            print("your guess is lower , try again ")
    except ValueError:
        print("your value is wrong  ")
    except KeyboardInterrupt:
        print("don t, quit game ")

