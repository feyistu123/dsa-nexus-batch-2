class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):       #custom comparison function
            xy = str(x) + str(y)
            yx = str(y) + str(x)
            if xy > yx:
                return -1  
            elif xy < yx:
                return 1  
            else:
                return 0
        nums_str = sorted(nums, key=cmp_to_key(compare))
        result = "".join(map(str, nums_str))
        if result[0] == '0' and len(result) > 1:
            return "0"
        return result
    
