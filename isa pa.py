##ATM

print("-----GIAN'S-----")
print("ATM MACHINE INC.")

p = int(input("Enter PIN:"))
crdts = 500000
if p == 1:
    print("Proceed")
    c = input("Enter code: ")
    if c == "x":
       print("hello")
       print("1. WITHDRAW")
       print("2. DEPOSIT")
       cx = int(input("CODE: "))
       if cx == 1:
           print("AVAILABLE BALANCE:", crdts)
           pcrdts = int(input("Enter money: "))

           mn = crdts - pcrdts
           print("AVAILABLE BALANCE", mn)
           print("THANKS FOR WITHDRAWING COME AGAIN")
       if cx == 2:
            print("AVAILABLE BALANCE:", crdts)
            dcrdts = int(input("Enter money: "))

            nm = dcrdts + crdts
            print("AVAILABLE BALANCE", nm)
            print("THANKS FOR DEPOSITING COME AGAIN")
        
           
else:
    print("error")
