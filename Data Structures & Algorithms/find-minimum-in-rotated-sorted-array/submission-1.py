class Solution:
    def findMin(self, nums: List[int]) -> int:

        mini = max(nums)

        for num in nums:

            mini = min(mini, num)

        return mini
        