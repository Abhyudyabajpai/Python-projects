premium_gd_shipping = 125.00

def ground_shipping(weight):
  cost = (weight * 4.00)+20+premium_gd_shipping
  return cost

# aq= shipping_cost(8.4)
# print(aq)
def drone_shipping(weight):
  cost = (weight*4.50)+0.00+premium_gd_shipping
  return cost

def shipping(weight):
  print("The most expensive method will cost "+ str(ground_shipping(weight)))
  print("The most cheapest method will cost "
  +str(drone_shipping(weight)))


ab = shipping(3.6)
