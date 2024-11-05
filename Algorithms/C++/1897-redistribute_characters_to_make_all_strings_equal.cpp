class Solution {
public:
    bool makeEqual(vector<string>& words) {
        unordered_map<char, int> map;

        for(int i = 0; i < words.size(); i++){
            for(int j = 0; j < words[i].size(); j++){
                if(map.contains(words[i][j])){
                    map[words[i][j]]++;
                
                }else{
                    map[words[i][j]] = 1;

                }

            }
        }

        for (const auto& pair : map) {
            if(pair.second % words.size() != 0){
                return false;
            } 
        }

        return true;
    }
};