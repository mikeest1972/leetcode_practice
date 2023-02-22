from typing import List
# O(n^2) complexity
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    
    def driver(self):
        nums = [3,3]
        target = 6
        res = self.twoSum(nums=nums,target=target)
        print(res)

Solution().driver()