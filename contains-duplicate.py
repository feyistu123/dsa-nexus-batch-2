class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)       #time O(n) space O(n)

        '''seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False'''
