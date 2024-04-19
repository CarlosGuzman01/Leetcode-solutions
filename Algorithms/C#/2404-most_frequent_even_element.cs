public class Solution {
    public int MostFrequentEven(int[] nums) {

        Dictionary<int, int> map = new Dictionary<int,int>();
        List<int> list = new List<int>();
        
        foreach(int i in nums){
            if(map.ContainsKey(i)){
                map[i]++;
            
            }else if(i % 2 == 0){
                map.Add(i, 1);
            }
        }

        if(map.Count == 0){
            return -1;
        }

        int a = int.MinValue;
        foreach(int i in map.Keys){
           if(map[i] > a){
            a = map[i];
            list.Clear();
            list.Add(i);
           
           }else if(map[list.ElementAt(0)] == map[i]){
            list.Add(i);
           }
        }

        if(list.Count == 0){
            return list.ElementAt(0);
        }else{
            return list.Min();
        }
        
    }
}