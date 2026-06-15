print("           Z.A Garments ")
print("           Murree Road ")
print("           Rawalpindi ")
print("           03001112223 ")
print("")
def invoice():
    total_items = []
    num_item = int(input(f"{"Enter items quantity" :<30} : "))
    print("")
    for i in range(num_item):
        item_name = input(f"{"Enter item name" :<30} : ")
        item_quantity = int(input(f"{"Enter item quantity" :<30} : "))
        item_price = int(input(f"{"Enter item price" :<30} : "))
        print(f"{item_name:<30} : {item_quantity} X {item_price}")
        print("-"*50)
        print(f"Total {item_name:<24} : {item_quantity * item_price}")
        print("")
        total_items.append(item_quantity * item_price)
        
    return total_items

items = invoice()
total = sum(items)
print(f"{"Total Price":<30} : {total}")

def apply_discount(total):
    discount = total * 0.10
    return discount

total_discount = apply_discount(total)
print(f"{"Total Discount":<30} : {total_discount}")

def price_after_discount(total, total_discount):
    after_discount = total - total_discount
    return after_discount

discounted_price = price_after_discount(total, total_discount)
print(f"{"Discounted Price":<30} : {discounted_price}")

def apply_tax(discounted_price):
    tax = discounted_price * 0.05
    return tax

total_tax = apply_tax(discounted_price)
print(f"{"Tax 5%":<30} : {total_tax}")

def bill(discount_price, total_tax):
    total_bill = discount_price + total_tax
    return total_bill
print("-"*50)
final_bill = bill(discounted_price, total_tax)
print(f"{"Final Bill":<30} : {final_bill}")