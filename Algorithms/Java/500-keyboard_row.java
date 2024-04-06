class Solution {
    public String[] findWords(String[] words) {

        String first = "qwertyuiop";
        String second = "asdfghjkl";
        String third = "zxcvbnm";
        
        HashSet<Character> firstRow = new HashSet<>();
        HashSet<Character> secondRow = new HashSet<>();
        HashSet<Character> thirdRow = new HashSet<>();

        for(char c: first.toCharArray()){
            firstRow.add(c);
        }

        for(char c: second.toCharArray()){
            secondRow.add(c);
        }

        for(char c: third.toCharArray()){
            thirdRow.add(c);
        }

        StringBuilder builder = new StringBuilder();;
        ArrayList<String> myList = new ArrayList<>();
        
        for(String s: words){

            for(char c: s.toCharArray()){
                if (!firstRow.contains(Character.toLowerCase(c))) {
                    builder.setLength(0);
                    break;
                
                }else{
                    builder.append(c);
                }
            }

            if(builder.length() != 0){
                myList.add(builder.toString());
                builder.setLength(0);
            }


            for(char c: s.toCharArray()){
                if (!secondRow.contains(Character.toLowerCase(c))) {
                    builder.setLength(0);
                    break;
                
                }else{
                    builder.append(c);
                }
            }

            if(builder.length() != 0){
                myList.add(builder.toString());
                builder.setLength(0);
            }


            for(char c: s.toCharArray()){
                if (!thirdRow.contains(Character.toLowerCase(c))) {
                    builder.setLength(0);
                    break;
                
                }else{
                    builder.append(c);
                }
            }


            if(builder.length() != 0){
                myList.add(builder.toString());
                builder.setLength(0);
            }

        }

        return myList.toArray(new String[myList.size()]);
        
    }
}