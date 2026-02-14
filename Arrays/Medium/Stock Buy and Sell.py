#brute approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #traversing the array twice using nested loops
        #i starts from 0 to n
        #j starts from i+1 to n
        #we check the profit by subtracting i from j and store it into a variable profit
        #we use another variable maxprofit to store the max profit between profit and maxprofit.

        n = len(prices)
        maxprofit = 0

        for i in range(n):
            for j in range(i+1, n):
                profit = prices[j] - prices[i]

                #taking the max profit
                maxprofit = max(profit, maxprofit)

        return maxprofit

#Optimal approach - using a single pointer.
#We can simultaneously compare the minimum price and the maxprofit while iterating through a single pass.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initialising the min price to a very large number
        min_price = float(inf)

        #initialising the max profit as 0, to use it for comparisons further
        max_profit = 0

        #traversing through the array
        for price in prices:
            #getting our current minimum price.
            if price < min_price:
                min_price = price
            else:
                #comparing the current max profit with the current price and the minimum price found so far.
                max_profit = max(max_profit, price - min_price)
            
        return max_profit
