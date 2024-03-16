class Solution {
    public boolean isHappy(int n) {

        HashSet<Integer> myHashSet = new HashSet<>();

        int total;

        while(!myHashSet.contains(n)){
            total = 0;
            
            myHashSet.add(n);

            while(n > 0){
                int digit = n % 10;
                total = total + (digit * digit);
                n = n / 10;

            }

            n = total;

            if(total == 1){
                return true;
            }
        } 
        
       return false;

    }
}