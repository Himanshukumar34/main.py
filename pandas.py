def student():
    try:
        name=str(input("Enter your name :"))
        num=int(input("Enter your no. subject  :"))
        marks_list=[]
        for i in range(num+1):
            marks=int(input("Enter your marks :"))
            marks_list.append(marks)
        with open("studnt.txt","a") as f:
            f.write(name+"\n") 
            f.write("Marks: " + ",".join(map(str, marks_list)) + "\n")
        print("your recorded ")
    except ValueError:
        print("invalid input")

            