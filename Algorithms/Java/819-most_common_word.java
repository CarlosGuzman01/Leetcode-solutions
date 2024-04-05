class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {

        
        HashSet<String> bannedWords = new HashSet<>();
        HashMap<String, Integer> countWord = new HashMap<>();
        int maxAmount = Integer.MIN_VALUE;
        String result = "";

        for(String s: banned){
            bannedWords.add(s);
        }

        for(String s: paragraph.toLowerCase().split("\\W+")){
            if(bannedWords.contains(s)){
                continue;
            }

            countWord.put(s, countWord.getOrDefault(s, 0) + 1);

            if(maxAmount < countWord.get(s)){
                maxAmount = countWord.get(s);
                result = s;
            }

            
        }

        return result;

        
        
    }
}