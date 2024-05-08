class Solution {
    public String thousandSeparator(int n) {
        
        if(n < 1000) return String.valueOf(n);
        
        StringBuilder sb = new StringBuilder();

        int counter = 1;
        while(n > 0){
            int p = n % 10;

            sb.append(p);

            if(counter == 3){
                sb.append('.');
                counter = 0;
            }

            n = n / 10;

            counter++;
        }

        if(!Character.isDigit(sb.charAt(sb.length() - 1))){

            sb.deleteCharAt(sb.length() - 1);
        }

        return sb.reverse().toString();
        
    }
}