class Solution {
    public String kthDistinct(String[] arr, int k) {

        LinkedHashMap<String, Integer> myMap = new LinkedHashMap<>();
        ArrayList<String> myList = new ArrayList<>();

        for (String s : arr) {
            myMap.put(s, myMap.getOrDefault(s, 0) + 1);
        }

        for(String s : myMap.keySet()){
            if (myMap.get(s) == 1) {
                myList.add(s);  
            }
        }

        if(myList.size() < k){
            return "";
        }

       return myList.get(k - 1);
        
    }
}