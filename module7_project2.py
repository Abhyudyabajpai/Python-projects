toppings = ['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']

prices = [2,6,1,3,2,7,2]

num_pizzas = len(toppings)

print("We sell "+str(num_pizzas)+" kinds of pizzas!")

pizzas = list(zip(prices,toppings))

print(pizzas)

pizzas.sort()
#print(pizzas)

cheapest_pizza = pizzas[0]

priciest_pizza = pizzas[-1]

three_cheapest = pizzas[:3]

print(three_cheapest)
#print(priciest_pizza)
num_two_dollar_slices = prices.count(2)

print(num_two_dollar_slices)


