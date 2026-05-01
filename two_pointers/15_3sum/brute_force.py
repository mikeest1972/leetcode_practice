class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        results = []
        numsLen = len(nums)
        for i in range(numsLen):
            for j in range(i,numsLen):
                for k in range(j,numsLen):
                    if i != j and i != k and j != k:
                        if (nums[i] + nums[j] + nums[k]) == 0:
                            res = sorted([nums[i],nums[j],nums[k]])
                            if res not in results:
                                results.append(res)
                        
        return results


# nums = [-1,0,1,2,-1,-4]
#nums = [0,1,1]
nums = [0,0,0]

a = Solution().threeSum(nums)
print(a)