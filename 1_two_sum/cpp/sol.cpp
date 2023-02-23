#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        int iterations = nums.size();
        
        for(int i = 0; i < iterations; i++)
        {
            for(int j = i+1; j < iterations; j++ )
            {
                if(nums[i] + nums[j] == target)
                {
                    
                    return vector<int> {i,j};
                }

            }

        }
        return v;
    }
};

int main()
{
    std::vector<int> v{ 2,7,11,15 };
    int target = 17;
    Solution s;
    std::vector<int>result =  s.twoSum(v,target);
    std::cout << "[" <<  result[0] <<  "," << result[1] << "]\n";

    return 0;
}