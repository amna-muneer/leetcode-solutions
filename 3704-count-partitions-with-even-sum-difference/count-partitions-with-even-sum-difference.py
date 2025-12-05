class Solution:
     def countPartitions(self, nums):
        n = len(nums)
        total = sum(nums)
        return (n - 1) if total % 2 == 0 else 0
