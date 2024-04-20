class Solution {
    public int maxNumberOfBalloons(String text) {

        int counter = 0;
        HashMap<Character, Integer> myMap = new HashMap<>();

        for (char c : text.toCharArray()) {
            myMap.put(c, myMap.getOrDefault(c, 0) + 1);
        }

        if (myMap.containsKey('b') && myMap.containsKey('a') && myMap.containsKey('l') && myMap.containsKey('o')
                && myMap.containsKey('n')) {
            while (myMap.get('b') >= 1 && myMap.get('a') >= 1 && myMap.get('l') >= 2 && myMap.get('o') >= 2
                    && myMap.get('n') >= 1) {

                counter++;

                myMap.put('b', myMap.get('b') - 1);
                myMap.put('a', myMap.get('a') - 1);
                myMap.put('l', myMap.get('l') - 2);
                myMap.put('o', myMap.get('o') - 2);
                myMap.put('n', myMap.get('n') - 1);

               

            }
        }

        return counter;
        
    }
}