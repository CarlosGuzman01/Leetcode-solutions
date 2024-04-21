class Solution {
    public String greatestLetter(String s) {

        ArrayList<Character> myList = new ArrayList<>();
        HashSet<Character> mySet = new HashSet<>();

        for(char c : s.toCharArray()){
            if(!mySet.contains(c) && (mySet.contains(Character.toUpperCase(c)) || mySet.contains(Character.toLowerCase(c)))){
                myList.add(Character.toUpperCase(c));
            }else{
                mySet.add(c);
            }
        }

          if(myList.isEmpty()){
            return "";
            }

        int max = Integer.MIN_VALUE;

        for(char c: myList){
            max = Math.max((int) max, (int) c);
        }

        return Character.toString((char) max);
    
    }
}