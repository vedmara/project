#carrots = int(input('How many carrots do you have? '))
#rabbits = 6

#if rabbits > carrots:
 #   print('There are not enough carrots')
#elif rabbits < carrots:
 #   print('There are too many carrots')
#else:
 #   print('You have the right number of carrots')

#clothes = [
 ### "t-shirt",
#]
#if clothes[0]== "shorts":
 #   clothes[0] = "warm coat"
#print(clothes)



#3shopping_list = ["milk", "bread", "sugar", "salt"]
#shopping_list.append("butter")
#if "bread" in shopping_list:
 #   print(shopping_list)
#else:
 #   print("don't forget a bread")

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = sum(costs)
print(total_cost)
total_cost = 0


for i in costs:
    total_cost += i
print(total_cost)
