fruit1 = "apple"
fruit2 = "banana"
fruit3 = "mango"

apple = 80
banana= 60
mango = 200

fruit = input("Which fruit you want (apple, mango, banana)")
money = int( input("Give me money"))

if fruit1==fruit:
    qty=int(input("qty : "))
    total = money - (qty*apple)  
    print( qty, "/kg apple. and your remaning amount ", total)