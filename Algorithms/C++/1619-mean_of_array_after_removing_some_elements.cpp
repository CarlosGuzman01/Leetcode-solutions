class Solution {
public:
    double trimMean(vector<int>& arr) {
        int count = 0;
        double total = 0;

        sort(arr.begin(), arr.end());

        int low = 0 + ((arr.size() * 5) / 100);
        int high = arr.size() - ((arr.size() * 5) / 100);

        for(int i = low; i < high; i++){
            total += arr[i];
            count++;
        }
        
       
        return total / count;
    }
};