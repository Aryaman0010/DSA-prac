# Two Sum Problem

## 📌 Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

---

## 💡 Approach (Brute Force)

* Iterate through each element using a loop.
* For every element, check all the elements ahead of it.
* If the sum equals the target, return their indices.

---

## 🧠 Algorithm

1. Loop through array using index `i`
2. For each `i`, loop through remaining elements using `j`
3. Check if `nums[i] + nums[j] == target`
4. If yes, return `[i, j]`

---

## ⏱ Time Complexity

* **O(n²)** — Two nested loops

## 📦 Space Complexity

* **O(1)** — No extra space used

---

## 🧪 Example

### Input

```
nums = [2, 7, 11, 15]
target = 9
```

### Output

```
[0, 1]
```

---

## 🧾 Code

```python
class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

---

## 🚀 Future Improvements

* Optimize using HashMap (O(n) solution)
* Add user input handling
* Add test cases

---

## 📁 How to Run (Optional Version)

```python
nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

sol = Solution()
print(sol.twoSum(nums, target))
```

---

## ✍️ Author

Aryaman
