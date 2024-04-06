class Solution {
    public String makeGood(String s) {

        Deque<Character> myQueue = new ArrayDeque<>();

        for(int i = 0; i < s.length(); i++){

            if(!myQueue.isEmpty() && 
            myQueue.peekLast() != s.charAt(i) &&
            Character.toLowerCase(myQueue.peekLast()) == Character.toLowerCase(s.charAt(i))
            ){
                myQueue.removeLast();

            }else{
                myQueue.add(s.charAt(i));
            }
        }

        StringBuilder build = new StringBuilder();

        for(char c: myQueue){
            build.append(c);
        }

       return build.toString();
        
    }
}