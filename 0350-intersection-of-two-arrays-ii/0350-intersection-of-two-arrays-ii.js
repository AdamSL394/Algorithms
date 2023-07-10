/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    const res = []
    hm = {}
    for (num of nums1){
        if (hm[num]){
            hm[num] += 1
        }else{
            hm[num] = 1
        }
    }
    
    for(num of nums2) {
        if(hm[num]){
            if (hm[num] > 0){
                res.push(num)
            }
            hm[num] -= 1
        }
        
    }
   
    return res
};