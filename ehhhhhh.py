##Massive task #6 store!

import sys
import time
print("================")
print("Fungo Store")
print("================")

words = "WELCOME TO BURGERAN NI EJOHN \n"
for char in words:
   time.sleep(0.01)
   sys.stdout.write(char)
   sys.stdout.flush()
input("Enter your name: ")
print("")
print("AVAILABLE ORDERS")
print("AM1 = Chicken with rice, ₱100")
print("AM2 = Hotdog with rice, ₱50")
print("AM3 = Pork with rice, ₱150")
print("AM4 = Beef with rice, ₱200")

print("")
def goods():

    food= input("What is your order: ")
    AM1 = ["Chicken with rice, ₱100"]
    AM2 = ["Hotdog with rice, ₱50"]
    AM3 = ["Pork with rice, ₱150"]
    AM4 = ["Beef with rice, ₱200"]

    hotdog  = food
    if hotdog == "AM1":
       print(AM1)
    if hotdog == "AM2":
       print(AM2)
    if hotdog == "AM3":
       print(AM3)
    if hotdog == "AM4":
       print(AM4)
    Prc = input("Enter Price: ₱")
    Qn = input("How many servings? ")
    aos = int(Prc) * int(Qn)
    Price = print("Total is: ₱", aos)
    cash = input("Enter Cash: ₱")
    change = int(cash) - int(aos)
    print("Change: ₱", change)
    finished = input("Do you still have a order? ")
    
goods()

