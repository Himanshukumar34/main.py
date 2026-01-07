import time
import winsound
time1=int(input("Enter your countdown in second : "))
for i in range(time1, 0 , -1):
    print("Time remaining :",i)
    time.sleep(1)
print("timesup")
winsound.Beep(1000,500)
time.sleep(1)
winsound.Beep(1000,500)
time.sleep(1)
winsound.Beep(1000,500)
time.sleep(1)



