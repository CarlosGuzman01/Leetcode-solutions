class Solution {
    public boolean isValid(String s) {

        Stack<Character> myStack = new Stack<>();
        HashMap<Character, Character> myMap = new HashMap<>();

        myMap.put('(', ')');
        myMap.put('[', ']');
        myMap.put('{', '}');

        if(s.length() % 2 != 0 ){
            return false;
        }

        if(!myMap.containsKey(s.charAt(0))){
            return false;
        }

        for(int i = 0; i < s.length(); i++){

            if(!myMap.containsKey(s.charAt(i))){

                if(myStack.empty()){
                return false;

                } else if(s.charAt(i) != myMap.get(myStack.pop())){
                return false; 
                }
            
            }else{
            myStack.push(s.charAt(i));
            
                
            }

    }

        return myStack.empty();


        
    }
}