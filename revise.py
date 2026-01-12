value=["apple","banana","papya","reddish",True]
print("the vlaue is ", value)
while True:
    print("main menu ")
    print("1. insert")
    print("2. delete")
    print("3. index")
    print("4. reverse")
    print("5. sort")
    print("6. clear")
    print("7. exit")
    choice=int(input("Enter your choice(1,2,3)"))
    if choice==1:
        inert=input("Enter your input")
        value.append(inert)
        print(value)
    elif choice==2:
        val=input("Enter your delete indexing or value")
        if val==str:
            value.remove(val)
            print(value)
        elif val==int:
            value.pop(val)
            print(value)
    elif choice==3:
        chr=str()

