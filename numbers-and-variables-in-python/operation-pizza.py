# look at chapter tree Atlanta pizza
number_of_pizzas = eval(input("how many pizzas do you want?"))

cost_per_pizzas = eval(input("how much does each pizza cost?"))

subtotal = number_of_pizzas * cost_per_pizzas

tax_rate = 0.08
sales_tax = subtotal * tax_rate

total = subtotal + sales_tax

print("the total cost is $", total)
print("this includes $", subtotal, "for pizza and")
print("$", sales_tax, "in sales tax.")
