class Solution {
public:
    string makeFancyString(string s) {

        if(s.size() <= 2){
            return s;
        }
        
        string ans (1, s[0]);
        char temp = s[0];
        int count = 1;

        for(int i = 1; i < s.size(); i++){
            
            if(temp == s[i]){
                count++;

            }else{
                count = 1;
                temp = s[i];
            }

            if(count >= 3){
                continue;
            }

            ans += s[i];

        }
        return ans;
    }
};