# Stock Prices

# This challenge, you’ll return the maximum profit possible for buying-and-selling a stock.

# The best function will be given a list of stock prices as they happened throughout the day:

# best([15, 10, 20, 22, 1, 9])
# It should return the maximum possible profit on the stock for that day. 
# For example, with these prices, our best option would have been to buy the stock at $10 
# and sell it at $22. So the profit would be $12:

# >>> best([15, 10, 20, 22, 1, 9])
# 12
# Best profit: $4 (buy at $1, sell at $5):

# >>> best([1, 2, 3, 4, 5])
# 4
# Other tests:

# >>> best([2, 3, 10, 6, 4, 8, 1])
# 8
# >>> best([7, 9, 5, 6, 3, 2])
# 2
# >>> best([0, 100])
# 100

# >>> best([5,4 ,3, 2, 1])
# 0

# >>> best([100])
# 0

# >>> best([100, 0])
# 0

def best(prices):

	curr_low = None
	max_profit = 0

	for p in prices:

		if not curr_low or p < curr_low:
			curr_low = p

		if (p-curr_low) > max_profit:
			max_profit = p-curr_low

	return max_profit


