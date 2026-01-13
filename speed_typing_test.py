import time
print("----SPEED TYPING TEST ------")
print("“Type the displayed text accurately and press Enter after completion. "
"The program will calculate typing speed, accuracy, and time taken, and then display the results.") #instruction for user
now=str(input("when you press enter your test is start :")) #start typing by enter
t1=time.time() # start a timer 
original_text="Screen par diya gaya text dhyan se aur sahi tarike se type karein. " \
"now you will go and other just play thing like me go for any"
print(original_text)
typed_text=str(input("now your test is start :"))
v1=time.time()-t1
print("Time ups")
original_words = original_text.split()
typed_words = typed_text.split()
correct_words = 0
for i in range(min(len(original_words), len(typed_words))):
     if original_words[i] == typed_words[i]:
      correct_words += 1 
print(f"you completed in time {v1}")
num1=v1/60
num2=(len(typed_text)/5)/num1
print(f"your WPM is {num2}")
num3=(correct_words/len(original_text))/100
print(f"your accurancy is {num3}")
