class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative number kabhi palindrome nahi
        if x < 0:
            return False
        
        # Numbers ending with 0 (except 0) cannot be palindrome
        if x % 10 == 0 and x != 0:
            return False
        
        reversed_half = 0
        
        # Reverse last half digits
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10
        
        # Check palindrome
        # Even length → x == reversed_half
        # Odd length → x == reversed_half // 10 (middle digit ignore)
        return x == reversed_half or x == reversed_half // 10
