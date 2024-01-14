# Ask the person how many pizzas they want, get the # with eval()
number_of_pizzas = eval(input("how many pizzas do you want?"))
# Ask for the menu cost of each pizza
cost_per_pizzas = eval(input("how much does each pizza cost?"))
# Calculate the total cost of the pizzas as our subtotal
subtotal = number_of_pizzas * cost_per_pizzas
# Calculate the sales tax owed, at 8% of the subtotal
tax_rate = 0.08 # we store 8% as the decimal value 0.08
sales_tax = subtotal * tax_rate
# Add the sales tax to the subtotal for the final total
total = subtotal + sales_tax
# Show the user the total amount due, including tax
print("the total cost is $", total)
print("this includes $", subtotal, "for pizza and")
print("$", sales_tax, "in sales tax.")
