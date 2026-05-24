from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums);
        n = len(nums)
        buckets =[];
        for _ in range(n+1):
            buckets.append([])

        for num, count in freq.items():
            buckets[count].append(num)

        
        result =[]
        for freq in range(n,0,-1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        
            

        