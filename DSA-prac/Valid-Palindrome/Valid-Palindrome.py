class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s="".join(c for c in s if c.isalnum()).lower()
        left=0
        right=len(s)-1
        while left<right:
            if s[left] !=s[right]:
                return False
            left +=1
            right -=1
        return True
    

if __name__ == "__main__":
    s= input("Enter Phrase :")
    sol= Solution()
    print(sol.isPalindrome(s))