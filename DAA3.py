def fractional_knapsack(capacity, items):

    # Sort items by profit/weight ratio
    items.sort(key=lambda item: item[2], reverse=True)

    total_profit = 0

    for item in items:

        profit, weight, ratio = item

        if capacity >= weight:
            total_profit += profit
            capacity -= weight

        else:
            fraction = ratio * capacity
            total_profit += fraction
            capacity = 0
            break

    return total_profit

n = int(input("Enter number of items: "))

items = []

for i in range(n):

    profit = int(input("Enter profit of item: "))
    weight = int(input("Enter weight of item: "))

    ratio = profit / weight

    items.append((profit, weight, ratio))

capacity = int(input("Enter knapsack capacity: "))

max_profit = fractional_knapsack(capacity, items)

print("\nMaximum Profit:", max_profit)