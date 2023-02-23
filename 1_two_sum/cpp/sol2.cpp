#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        int iterations = nums.size();
        
        for(int i = 0; i < iterations; i++)
        {

        }
        
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