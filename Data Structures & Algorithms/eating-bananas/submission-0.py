from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            total = 0
            for pile in piles:
                total += ceil(pile / k)

            return total

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            if hours_needed(mid) <= h:
                right = mid
            else:
                left = mid +1 
        return left
        