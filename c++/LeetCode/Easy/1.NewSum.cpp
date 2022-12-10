// 1. Two Sum

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

// https://leetcode.com/problems/two-sum/description/



#include "stdio.h"
#include "iostream"

using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> tmp;
        
        for(int i=0; i<nums.size(); i++){
            int minusTmp = target - nums[i]
            tmp.push_back(minusTmp);
        }

        cout << tmp
        
        return res;
    }
};


// O(n^2) Solution
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        
        for(int i=0; i<nums.size()-1; i++){
            for(int j=i+1; j < nums.size(); j++){
                if(nums[i] + nums[j] == target){
                    res.push_back(i);
                    res.push_back(j);
                }
            }
        }
        
        return res;
    }
};