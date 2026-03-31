class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        unique_count = Counter(nums)
        unique = []
        
        for key, value in unique_count.items():
            heapq.heappush(unique, (-value, key))

        res = []
        while len(res) < k:
            res.append(heapq.heappop(unique)[1]) 
        
        return res