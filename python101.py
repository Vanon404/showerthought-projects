 



order_total = 0

menu = {

    'pizza' :  100,
    'coffee' : 50,
    'cake' : 70,
    'chips' : 30,
    'fish' : 120,
}

print ("welcome to our restaurant")
print ("pizza: 100")
print ("coffee: 50")
print ("cake: 70")
print ("chips: 30")
print ("fish: 120")

while True:

    item_1 = input("enter an item: ")

    if item_1 in menu:
        order_total += menu [item_1]
        print ("your item {item_1} added to order")

    else:
        print(f"Ordered item{item_1} is not available in the menu")

    anotheritem = input("do you want to order another item? yes/no: ")

    if anotheritem.lower() != "yes":
        break
    
    

print (f"your total order to pay is {order_total} quid") 