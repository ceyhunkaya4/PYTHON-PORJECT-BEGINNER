import random

name_string = input("give me everybody's names, with separated by a comma. ")
names = name_string.split(",")

num_items = len(names)
random_choice = random.randint(0,num_items-1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is goıng to pay")