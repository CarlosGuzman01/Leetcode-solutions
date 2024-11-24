class Solution {
public:
    int hardestWorker(int n, vector<vector<int>>& logs) {
        int max_time = logs[0][1];
        int max_id = logs[0][0];

        for(int i = 1; i < logs.size(); i++){
            int val = logs[i][1] - logs[i - 1][1];

            if(max_time == val){
                if(max_id > logs[i][0]){
                    max_id = logs[i][0];
                }
            }else if(max_time < val){
                max_time = val;
                max_id = logs[i][0];

            }

        }

        return max_id;
    }
};