class Solution {
    public boolean digitCount(String num) {

        HashMap<Integer, Integer> myMap = new HashMap<>();

        for (char c : num.toCharArray()) {
            int current = Character.getNumericValue(c);
            myMap.put(current, myMap.getOrDefault(current, 0) + 1);
        }

        int count = 0;
        for(int i = 0; i < num.length(); i++) {
            if(myMap.containsKey(i)){
                count = myMap.get(i);

            }else{
                count = 0;
            }

            if(Character.getNumericValue(num.charAt(i)) != count ) return false;
        }

        return true;
    }
}