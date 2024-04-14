class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {

        HashMap<String, Integer> myMap = new HashMap<>();
        ArrayList<String> myList = new ArrayList<>();
        
        String s3 = s1 + " " + s2;

        String[] words = s3.split("[\\W]");

        for(String s: words){
            myMap.put(s, myMap.getOrDefault(s, 0) + 1);
        }

        for(int i = 0; i < words.length; i++){
            if(myMap.get(words[i]) == 1){
                myList.add(words[i]);
            }
        }

        return myList.toArray(new String[myList.size()]);
        
    }
}