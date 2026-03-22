# Contains Duplicate

## 📌 Problem

Given an array of integers `nums`, return `True` if any value appears at least twice, and `False` if all elements are distinct.

---

## 💡 Approach (Using Set)

* Convert the list into a set (removes duplicates)
* Compare the size of original list and set
* If sizes are different → duplicates exist

---

## ⏱ Complexity

* Time: **O(n)**
* Space: **O(n)**

---

## 🧪 Example

### Input

```id="p8h1ye"
nums = [1, 2, 3, 1]
```

### Output

```id="d7x4nm"
True
```

---

## 🧾 Code

```python id="4v2c9j"
class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
```

---

## ✍️ Author

Aryaman
