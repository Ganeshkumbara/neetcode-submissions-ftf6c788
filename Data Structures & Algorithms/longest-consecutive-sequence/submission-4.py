class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = sorted(nums)
        longest_streak = 0
        length = 0
        if not nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                length += 1
            else:
                length = 0
            
            longest_streak = max(length, longest_streak)
        
        return longest_streak +1


        # hash_set = set(nums)

        # longest_streak = 0
        # for num in nums:
        #     if num - 1 not in hash_set:
        #         current_num = num
        #         current_streak = 1

        #         while current_num + 1 in hash_set:
        #             current_num += 1
        #             current_streak += 1
                
        #         longest_streak = max(longest_streak, current_streak)

        # return longest_streak

