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

def apply_discount(bill):
    dist = bill * 0.10
    return dist

discount = apply_discount(bill)
print(f"Total Discount : {discount}")


def price_after_discount(bill, discount):
    dist_price = bill - discount
    return dist_price

discounted_price = price_after_discount(bill, discount)
print(f"Price After Discount : {discounted_price}")


def apply_tax(discounted_price):
    tax = discounted_price * 0.05
    return tax

applied_tax = apply_tax(discounted_price)
print(f"Total Tax : {applied_tax}")


def last_bill(applied_tax, discounted_price):
    bill = discounted_price + applied_tax
    return bill

f_bill = last_bill(applied_tax,discounted_price)
print(f"Final Bill : {f_bill}")