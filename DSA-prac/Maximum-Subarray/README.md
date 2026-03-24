# Maximum Subarray

## 📌 Problem

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the **largest sum**, and return its sum.

---

## 💡 Approach (Kadane’s Algorithm)

* Traverse the array once
* At each element:

  * Decide whether to:

    * Start a new subarray
    * Or continue the previous one
* Keep track of:

  * Current subarray sum
  * Maximum sum found so far

---

## 🧠 Algorithm

1. Initialize:

   * `current_sum` = first element
   * `max_sum` = first element
2. Traverse from second element:

   * `current_sum = max(num, current_sum + num)`
   * Update `max_sum`
3. Return `max_sum`

---

## ⏱ Complexity

* Time: **O(n)**
* Space: **O(1)**

---

## 🧪 Example

### Input

```
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

### Output

```
6
```

### Explanation

Subarray `[4, -1, 2, 1]` has the maximum sum = `6`

---

## 🧾 Code

```python
class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
```

---

## 🧠 Key Concept

* Dynamic Programming
* Greedy decision at each step

---

## ✍️ Author

Aryaman
