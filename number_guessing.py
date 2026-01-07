import random
import time
import_random=random.randint(1,100)
attempts=0
try:
   while True:
       user_input=int(input("Enter your guess:"))
       time.sleep(1)
       attempts+=1
       if user_input==import_random:
          print("🎉you guess right num,congrats",import_random)
          break
       elif user_input>import_random:
          print("your nunber is high,try again")
       elif user_input<import_random:
          print("your guess is low,try again")
   print("your win in  ",attempts ,"turn")
except ValueError:
   print("invalid input")




