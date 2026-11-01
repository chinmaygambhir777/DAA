def knapsack(W, wt, val, n):

    # Create DP table
    dp = [[0 for x in range(W + 1)]
          for x in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):

        for w in range(1, W + 1):

            if wt[i - 1] <= w:

                include = val[i - 1] + dp[i - 1][w - wt[i - 1]]

                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:

                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

n = int(input("Enter number of items: "))

val = []
wt = []

for i in range(n):

    profit = int(input("Enter profit: "))
    weight = int(input("Enter weight: "))

    val.append(profit)
    wt.append(weight)
    
W = int(input("Enter knapsack capacity: "))

max_profit = knapsack(W, wt, val, n)

print("\nMaximum Profit:", max_profit)