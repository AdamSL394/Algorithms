

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer,Integer> hash = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            if (hash.containsKey(target - nums[i])){
                int toReturn[] = {hash.get(target - nums[i]),i};
                return toReturn;
            }
            hash.put(nums[i],i);
        }

        return new int[] {};
    }
}