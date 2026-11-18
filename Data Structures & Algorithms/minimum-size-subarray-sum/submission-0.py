class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = len(nums) + 1
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            while target <= total:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if res == len(nums) + 1 else res 
        
        