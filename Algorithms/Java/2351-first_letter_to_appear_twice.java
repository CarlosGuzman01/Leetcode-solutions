import java.util.HashSet;

class Solution {
    public char repeatedCharacter(String s) {
        

        HashSet myHashSet = new HashSet<>();

       for(int i = 0; i < s.length(); i++){

        if(myHashSet.contains(s.charAt(i))){
            return s.charAt(i);
        }


        myHashSet.add(s.charAt(i));

       }

       return 'a';
    }
}