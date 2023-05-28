# 💡 You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# **Example :**
#
# Input: prices = [7,1,5,3,6,4]
#
# Output: 5
#
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def get_max_profit(price_list):
    max_profit = 0
    min_price = float('inf')

    for i in range(len(price_list)):
        if min_price > price_list[i]:
            min_price = price_list[i]
        elif price_list[i] - min_price > max_profit:
            max_profit = price_list[i] - min_price

    return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(get_max_profit(prices))
