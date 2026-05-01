# 3Sum

https://leetcode.com/problems/3sum/?envType=problem-list-v2&envId=oizxjoit

sum up nums num[i] num[j] num[k] i,j,k are all diffrent can't be equale to eachother
sum = 0
return all tripplets [[a,b,c] [d,e,f]....]

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


store solutions some how? list of lists? how do we handle permutations maybe a list of sets

brute force 

resutls = [[]]

for i
    for j
        for k
            num[i] + num[j] + num[k] = 0 then store each num as a list
return results

the prob is premutations 


So the way of solving this efficiently is by sorting the array and idividing the problem into a two sum

num a is the target and you skip if the target is repeated. then using two pointers you add the mand incremtn l or r depdning if the sum > 0 or < 0