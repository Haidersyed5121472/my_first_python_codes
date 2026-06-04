# Garments Shop Invoice Generator

def invoice(shirt_quantity, shirt_price, trouser_quantity, trouser_price):
    return (shirt_quantity * shirt_price) + (trouser_quantity * trouser_price)

shirt_quantity = int(input("Enter shirt quantity: "))
shirt_price = int(input("Enter shirt price: "))
shirt_total = (shirt_quantity * shirt_price)
print(f"Shirt Total : {shirt_total}")
trouser_quantity = int(input("Enter trouser quantity: "))
trouser_price = int(input("Enter trouser price: "))
trouser_total = (trouser_quantity * trouser_price)
print(f"Trouser Total : {trouser_total}")
bill = invoice(shirt_quantity , shirt_price , trouser_quantity , trouser_price)
print(f"Total Bill : {bill}")