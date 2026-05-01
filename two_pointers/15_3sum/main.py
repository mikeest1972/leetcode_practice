class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        results = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    # append result
                    results.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1

                                        
        return results
    
    def bubble_sort(self,nums: list[int]) -> list[int]:
        pass


nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
# nums = [0,0,0,0]

a = Solution().threeSum(nums)
print(a)