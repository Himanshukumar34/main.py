# age eligibility
try :
    age=int(input("Enter your age :"))
    if age<18:
        print("you are not eligible ")
    else:
        print("you are elgibile ")
except ValueError:
    print("you enter invalid input")
except KeyboardInterrupt:
    print("you not quit ")