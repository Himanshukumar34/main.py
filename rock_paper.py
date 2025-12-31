import random 
while True:
    try: 
       num1=random.choice(("rock","paper","scissor"))
       choice=str(input("ENter your choice  ( rock , paper , scissor )"))
       if choice not in ("rock ,paper , scissor"):
         print("you enter invalid ")
         continue
       if choice==num1:
         print("tie, Try again",num1)
       elif choice=="rock" and num1=="paper":
         print("you lose try again ",num1)
       elif choice=="scissor" and num1=="rock":
          print("you lose try agian", num1)
       elif choice =="paper" and num1=="scissor":
        print("yur lose Try again", num1)
       else:
        print("you win",num1)
        break 
    except ValueError:
      print("invalid input")
    except KeyboardInterrupt:
      print("don,t quit ")

