
class Solution {
    public List<String> fizzBuzz(int n) {

        List<String> answer = new ArrayList<>();

        int value = 1;
        for(int i = 0; i < n; i++){

            if(value % 3 == 0 && value % 5 == 0){
                answer.add("FizzBuzz");

            }else if(value % 3 == 0){
                answer.add("Fizz");
            
            }else if(value % 5 == 0){
                answer.add("Buzz");

            }else{
              answer.add(String.valueOf(value));
            }

            value++;
        }

        return answer;
    }
}