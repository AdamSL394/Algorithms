/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    res = nums.length

    for (i in nums){
        res += (i - nums[i])
    }
    
    return res
};