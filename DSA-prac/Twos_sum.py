class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(0, length):
            for j in range(i + 1, length):
                if (nums[i] + nums[j] == target):
                    return [i, j]

if __name__ == "__main__":
    nums=list(map(int,input("Enter numbers :").split()))
    target=int(input("Enter target :"))
    sol = Solution()
    result = sol.twoSum(nums, target)
    print("Indexs are:", result)