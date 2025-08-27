class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total_coins = 0
        left, right = 0, len(piles) - 2
        
        while left < right:
            total_coins += piles[right]
            left += 1
            right -= 2
        return total_coins
