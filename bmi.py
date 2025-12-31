# bmi machine
weight=int(input("Enter your weight:"))
height=float(input("Enter your height in foot :"))

metre=height*0.3048

square=metre*metre

Bmi=(weight/square)

if Bmi<=18.5:
    print(Bmi,"under weight")

elif Bmi<=24.9 and Bmi>=18.5:
    print(Bmi,"Normal weight")

elif Bmi>=25.9 and Bmi<=29.9:
    print(Bmi,"over weight")

else:
    print(Bmi,"obese person")

