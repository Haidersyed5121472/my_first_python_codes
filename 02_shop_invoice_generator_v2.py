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
total_bill = invoice(shirt_quantity , shirt_price , trouser_quantity , trouser_price)
print(f"Total Bill : {total_bill}")

def apply_discount(total_bill):
    discounted_amount = total_bill * 0.10
    return discounted_amount

discount = apply_discount(total_bill)
print(f"Total Discount : {discount}")


def price_after_discount(total_bill, discount):
    after_discount_amount = total_bill - discount
    return after_discount_amount

final_price_after_discount = price_after_discount(total_bill, discount)
print(f"Price After Discount : {final_price_after_discount}")


def apply_tax(final_price_after_discount):
    tax = final_price_after_discount * 0.05
    return tax

applied_tax = apply_tax(final_price_after_discount)
print(f"Total Tax : {applied_tax}")


def final_amount(applied_tax, final_price_after_discount):
    bill_amount = final_price_after_discount + applied_tax
    return bill_amount

final_bill = final_amount(applied_tax,final_price_after_discount)
print(f"Final Bill : {final_bill}")