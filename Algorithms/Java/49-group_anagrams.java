class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, ArrayList<String>> finalMap = new HashMap<>();
        ArrayList<String> list;

        for(String s: strs){
            String p = helper(s);

            if(finalMap.containsKey(p)){
                finalMap.get(p).add(s);

            
            }else{
                list = new ArrayList<>();
                list.add(s);
                finalMap.put(p, list);
            }

        }

        ArrayList<List<String>> finalList = new ArrayList<>();

        for(String s : finalMap.keySet()){
            finalList.add(finalMap.get(s));
        }


        return finalList;

    }

    public static String helper(String s){
        
        int[] array = new int[26];
        StringBuilder sb = new StringBuilder();

        for(char c: s.toCharArray()){
            array[c - 'a']++;
        }

        int l = 'a';
        for(int i: array){
            sb.append(l);
            sb.append(Integer.toString(i));
            l++; 
        }

        return sb.toString();
    }
}