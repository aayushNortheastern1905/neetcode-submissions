import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return [item for item, count in heapq.nlargest(k,freq.items(), key = lambda x: x[1])]

        