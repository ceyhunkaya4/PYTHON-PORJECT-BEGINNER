import random

dizi_listesi = ["Netflix" , "Disney" , "Amazon"]
num = len(dizi_listesi)
random_dizi = random.randint(0,num -1)

watch = dizi_listesi[random_dizi]

print(watch)