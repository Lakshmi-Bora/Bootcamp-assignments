''' This programme is being written for a cafe 
    to calculate the total worth of the stock'''

item_list = ["Hot Chocolate", "Espresso", "Latte", "Iced Coffee"
              , "Iced Tea", "Crossiant", "Sandwich", "Muffin"
              , "Waffle", "Breakfast Wrap"
              ]
price_list = [3.60, 2.30, 3.50, 3.50, 3.15, 2.15, 3.85, 2.75, 1.85, 4.85]
stock_list = [200, 125, 150, 100, 100, 100, 75, 50, 75, 50]

''' Creating a dictionary with items as keys 
    and corresponding prices as values '''
price_dict = {item_list[i]:price_list[i] for i in range(len(item_list))}

''' Creating a dictionary with items as keys 
    and corresponding stock as values '''
stock_dict = {item_list[i]:stock_list[i] for i in range(len(item_list))}

# Calculating the total stock worth in the cafe
stock_worth = [round(price_dict[i] * stock_dict[i], 2) for i in item_list]

print(f"{'Item': ^10} {'Price': ^20} {'Stock': ^5} {'Stock Worth': ^20}")

for i in range(len(item_list)):

    print(f"{item_list[i]: <15} £{price_dict[item_list[i]]:>6.2f}",end=' ')
    print(f"{stock_dict[item_list[i]]: >13}{'£':>7}{stock_worth[i]:>9.2f}")

print()
total_stock_worth = sum(stock_worth)
print(f"Total stock worth is: £{total_stock_worth:.2f}")
