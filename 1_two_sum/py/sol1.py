from typing import List
# O(n^2) complexity
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hash_map = {} # val , index
       for i in range(len(nums)):

        targetVal = target - nums[i]
        # checks if the val we are looking for is in hashmap
        if targetVal in hash_map:
            # if found we can add them so return the indices
            return [hash_map[targetVal],i]
        else:
            # not in map so add it
            hash_map[nums[i]] = i
    
    def driver(self):
        nums = [3,2,4]
        target = 6
        res = self.twoSum(nums=nums,target=target)
        print(res)

Solution().driver()