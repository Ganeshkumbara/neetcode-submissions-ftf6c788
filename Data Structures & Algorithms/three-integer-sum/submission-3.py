class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 2):
            current_num = nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                triplate_check = sorted([current_num, nums[left], nums[right]])
                if sum(triplate_check) == 0 and left != right and left != i and right != i:
                    if triplate_check not in result:
                        result.append(triplate_check)
                
                if sum(triplate_check) < 0:
                    left += 1
                else:
                    right -= 1
        
        return result