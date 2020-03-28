'''
Invalid Example:
  Take Out Orders: [1, 3, 5]
  Dine In Orders: [2, 4, 6]
  Served Orders: [1, 2, 4, 6, 5, 3]

Valid Example
  Take Out Orders: [17, 8, 24]
  Dine In Orders: [12, 19, 2]
  Served Orders: [17, 8, 12, 19, 24, 2]
'''


def check_order_validity(take_out_orders, dine_in_orders, served_orders):
  take_out_i = 0
  dine_in_i = 0
  take_out_next = take_out_orders[take_out_i]
  dine_in_next = dine_in_orders[dine_in_i]
  for i in range(len(served_orders)):
    order = served_orders[i]
    if order != dine_in_next and order != take_out_next:
      return False
    if order == dine_in_next and dine_in_i < len(dine_in_orders):
      dine_in_i += 1
      dine_in_next = dine_in_orders[dine_in_i] if dine_in_i < len(dine_in_orders) else dine_in_next
    if order == take_out_next and take_out_i < len(take_out_orders):
      take_out_i += 1
      take_out_next = take_out_orders[take_out_i] if take_out_i < len(take_out_orders) else take_out_next
  return True

# take_out = [17, 8, 24]
# dine_in = [12, 19, 2]
# served = [17, 8, 12, 19, 24, 2]
take_out = [1, 3, 5]
dine_in = [2, 4, 6]
served = [1, 2, 4, 6, 5, 3]

print(check_order_validity(take_out, dine_in, served))