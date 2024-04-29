class Solution {
    public int addedInteger(int[] nums1, int[] nums2) {
        
        int num2 = 0;

        for(int i: nums2){
            num2 = num2 + i;
        }

          for(int i: nums1){
            num2 = num2 - i;
        }

        return num2/nums1.length;

    }
}