print("Welcome to Pizza Order ")
size = input("What size do you want pizza ? S, M or L ")
add_pepperoni = input("Do you want pepperoni ? Y or N ")
extra_cheese = input("Do you want extra cheese ? Y or N ")
extra_xxl = input("Would you like to enlarge your menu with $4 difference ? Y or N ")

bill = 0
if size == "S" :
 bill += 15
elif size == "M" :
    bill+= 20
else :
    bill+= 25
if add_pepperoni == "Y" :
    if size == "S" :
     bill+= 2
    else :
     bill+= 4

if extra_cheese == "Y" :
    if size == "S" :
        bill+= 2
    elif size == "M" :
         bill+= 3
    elif size == "L" :
        bill+= 4

if extra_xxl == "Y" :
     bill+= 4
else :
     bill+= 0  



print(f"Your final bill is ${bill}")