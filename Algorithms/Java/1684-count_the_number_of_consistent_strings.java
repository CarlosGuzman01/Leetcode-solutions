

class Solution {
    public int countConsistentStrings(String allowed, String[] words) {

        HashSet<Character> mySet = new HashSet<>();
        int result = 0;

        for(char c: allowed.toCharArray()){
            mySet.add(c);
        }

        for(String s: words){

            result++;
            for(char c: s.toCharArray()){
                if(!mySet.contains(c)){
                    result--;
                    break;
                }
            }
        }

        return result;
    }
        
    }
