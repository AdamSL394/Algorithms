#include<stdio.h>
#include <map>
#include<iostream>    
#include<vector> 
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> missing;
        std::vector<int> myvec;

        for (int i = 0; i < nums.size(); i++){
            if (missing.find(target - nums[i]) == missing.end()){
                 missing[nums[i]] = i;
            }
            else
                return {missing[target - nums[i]], i};
        }

        return {-1,-1};
    }
};