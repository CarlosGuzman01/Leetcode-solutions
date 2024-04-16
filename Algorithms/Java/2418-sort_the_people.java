class Solution {
    public String[] sortPeople(String[] names, int[] heights) {

        HashMap<Integer, Integer> myMap = new HashMap<>();
        String[] result = new String[names.length];

        int i = 0;
        for(int value : heights){
            myMap.put(value, i);

            i++;
        }

        Arrays.sort(heights);


        i = 0;
        for(int j = names.length - 1; j >= 0; j--){
            result[i] = names[myMap.get(heights[j])];

            i++;
        
        }


        return result;
        
    }
}