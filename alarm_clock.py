import datetime
import winsound
while True:
    now = datetime.datetime.now()
    num1=now.strftime("%H:%M:%S") #add this line with chat gpt
    num2=int(input("Enter your time in hour  :"))
    num3=int(input("Enter your time in minute :"))
    num4=int(input("Enter your time in sec :"))
    num5=f"{num2}:{num3}:{num4}"
    if num1==num5:
        winsound.Beep(1000,500)
        break

