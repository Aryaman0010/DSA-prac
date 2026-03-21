class Solution(object):
    def maxProfit(self, prices):
      min_price=prices[0]
      max_profit=0
      for price in prices:
         if min_price>price:
            min_price=price
         else:
            profit=price-min_price
            if profit>max_profit:
                max_profit=profit
      return max_profit
    
if __name__ == "__main__":
   prices=list(map(int,input("Enter Prices :").split()))
   sol= Solution()
   result= sol.maxProfit(prices)
   print("Maximum Profit : ",result)
    