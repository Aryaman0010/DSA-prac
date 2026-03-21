# Best Time to Buy and Sell Stock

## 📌 Problem Statement

Given an array `prices` where `prices[i]` is the price of a stock on the `i-th` day, find the maximum profit you can achieve.

You may choose **one day to buy** and **one different day to sell** in the future.

If no profit is possible, return `0`.

---

## 💡 Approach (Optimal - One Pass)

* Track the **minimum price** seen so far.
* For each price:

  * Calculate potential profit (`current price - min price`)
  * Update maximum profit if higher
* Return the maximum profit

---

## 🧠 Algorithm

1. Initialize:

   * `min_price` = first element
   * `max_profit` = 0

2. Traverse the array:

   * If current price < `min_price` → update `min_price`
   * Else:

     * Calculate profit
     * Update `max_profit` if needed

3. Return `max_profit`

---

## ⏱ Time Complexity

* **O(n)** — Single pass through the array

## 📦 Space Complexity

* **O(1)** — No extra space used


## 🧾 Code

```python
class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit


if __name__ == "__main__":
    prices = list(map(int, input("Enter Prices : ").split()))
    sol = Solution()
    result = sol.maxProfit(prices)
    print("Maximum Profit :", result)
```

---

## 🚀 Key Concepts

* Greedy Algorithm
* Array Traversal
* Optimization (O(n) solution)

---

## ❗ Edge Cases

* Prices always decreasing → Output = `0`
* Single element → No transaction possible


---

## ✍️ Author

Aryaman
