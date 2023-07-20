# You are given an array prices where prices[i] is the price 
# of a given stock on the ith day.

# You want to maximize your profit by 
# 1) choosing a single day to buy one stock and 
# 2) choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, current_profit = 0, 0
        left_ptr = 0

        # while right_ptr < len(prices)
        for right_ptr in range(1, len(prices)):

            # for max profit right-ptr value should be bigger than left_ptr value
            # cause you have to buy first (with low value) and sell later (with high value)
            if prices[left_ptr] < prices[right_ptr]:
                current_profit = prices[right_ptr] - prices[left_ptr]
                max_profit = max(max_profit, current_profit)
            else:
                # prices[left_ptr] > prices[right_ptr]:
                # here right-ptr value is a new min, so we need to change left_ptr
                left_ptr = right_ptr
        
        return max_profit
        

