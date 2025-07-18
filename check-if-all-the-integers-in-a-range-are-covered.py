class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered_numbers = set()
        for start, end in ranges:
            for i in range(max(left, start), min(right, end) + 1): 
                covered_numbers.add(i)
        for i in range(left, right + 1):
            if i not in covered_numbers:
                return False 
        return True 
