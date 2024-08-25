#
#Part : Python string Formatting
#

price = 60
txt = f"price is {price} bath."
print(txt)
txt = f"price is {price : .2f} bath."
print(txt)


price = 50
tax = 0.25
txt = f"price is {price + (price * tax)} baht."
print(txt)


price = 10000
txt = f"price is {price: ,} baht."
print(txt)
