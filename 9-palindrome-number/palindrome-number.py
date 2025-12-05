class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert number to string and compare with its reverse
        s = str(x)
        return s == s[::-1]

