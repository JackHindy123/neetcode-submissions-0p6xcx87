class Solution {
    public boolean hasDuplicate(int[] nums) {
        int index  = 0;
        while(index < nums.length){
            for (int i = 0; i < nums.length; i++){
                if (i != index){
                    if (nums[i] == nums[index])
                        return true;
                }
            }
            index++;
        }
        return false;
    }
}