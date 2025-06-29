import random


def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max < 1000 and min < quantity < max:
        results_list = list(range(min, max))
        results = random.sample(results_list, quantity)
        return results
    else: return []
      

print(get_numbers_ticket(1, 100, 6))