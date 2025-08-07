class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        min_common = float("inf")
        set2 = set(nums2)
        for num in nums1:
            if num in set2:
                min_common = min(min_common, num)
        
        return min_common if min_common != float("inf") else -1
