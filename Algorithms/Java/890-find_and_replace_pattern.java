class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {

       
        String p = normalize(pattern);

        List<String> ans = new ArrayList<String>();
        for (String word : words)
            if (p.equals(normalize(word))) ans.add(word);
        return ans;
    }


    public String normalize(String pattern) {

        HashMap<Character, Integer> map = new HashMap<>();
        StringBuilder ans = new StringBuilder();

        int len = pattern.length();

       

        for(int i = 0; i < len; i++){
            map.put(pattern.charAt(i), map.getOrDefault(pattern.charAt(i), i));
            ans.append(map.get(pattern.charAt(i)));
        }


        return ans.toString();


    }
        
    
}