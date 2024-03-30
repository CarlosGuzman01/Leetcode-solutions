class Solution {
    public int maxArea(int[] height) {

        int maxArea = Integer.MIN_VALUE;
        int left = 0;
        int right = height.length - 1;


        for(int i = 0; i < height.length; i++){
            int width = right - left;
            int length = Math.min(height[left], height[right]);

            if(maxArea < width * length ){
                maxArea = width * length;
            }

            if(height[left] > height[right]){
                right--;
            
            }else{
                left++;
        
            }
        }

        return maxArea;


        
    }
}