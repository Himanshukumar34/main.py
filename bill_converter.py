# Welcome to Shopping Bill Calculator!

# Enter item name: Apple
# Enter price: 100
# Enter quantity: 2
# Do you want to add another item? yes

# Enter item name: Milk
# Enter price: 50
# Enter quantity: 1
# Do you want to add another item? no

# Your total bill is ₹250
# Discount Applied: ₹0
# Final Bill: ₹250
# Thank you for shopping with us!

print("Welome to shopping bill converter ")
count=0
while True:
    num1=str(input("Enter your item: "))
    price=int(input("Enter your price:"))
    quantity=int(input("Enter your quantity:"))
    num3=str(input("Do you want to add another item :"))
    cost=price*quantity
    count+=cost   
    if num3=="no":
        break
print("your total bill is ",count)

discount = 0
if count > 1000:
    discount = count * 0.1  # 10% discount
elif count > 500:
    discount = count * 0.05  # 5% discount

final_amount = count - discount
print("your total bill is ",final_amount)
