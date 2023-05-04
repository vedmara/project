#price = input('How much is a burger? ')
#vegetarian = input('Is there a vegetarian option? (y/n) ')
#within_budget = float(price) <= 10.00
#has_vegetarian = vegetarian == 'y'
#is_good_choice = within_budget and has_vegetarian
#if is_good_choice == 'True':  
 #   print('Restaurant meets criteria: {}'.format(is_good_choice))
#else:
#    print('It is no good choice!')

meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')
discount_applicable = discount_choice == 'y'
if discount_applicable == 'True':
    price = meal_price * 0.9
else:
    price = meal_price
print(price)