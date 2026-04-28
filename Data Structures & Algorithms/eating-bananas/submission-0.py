class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_consume(k):
            hours = 0
            for pile in piles:
                hours += pile // k
                if pile % k != 0:
                    hours += 1
                if hours > h:
                    return False
            return True

        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = left + (right - left) // 2 
            if can_consume(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans 