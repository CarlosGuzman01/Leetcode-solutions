public class Solution {
    public int CountWords(string[] words1, string[] words2) {


        
        Dictionary<string, int> dic1 = new Dictionary<string, int>();
        Dictionary<string, int> dic2= new Dictionary<string,int>();

        int counter = 0;
        string[] reference;

        if(words1.Length < words2.Length){
            reference = words1;
        }else{
            reference = words2;
        }

        foreach(string word in words1){
            if(dic1.ContainsKey(word)){
                dic1[word]++;
            }else{
                dic1.Add(word, 1);
            }
        }

        foreach (string word in words2){
            if(dic2.ContainsKey(word)){
                dic2[word]++;
            }else{
                dic2.Add(word, 1);
            }
        }

        for(int i = 0; i < reference.Length; i++){
            if(dic1.ContainsKey(reference[i]) && dic2.ContainsKey(reference[i])){
                if(dic1[reference[i]] == 1 && dic2[reference[i]] == 1){
                    counter++;
                }
            }
        }
        
        return counter;

        
    }
}