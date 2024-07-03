class Solution {
public:
    char repeatedCharacter(string s) {
        
        std::unordered_set<char> mySet;
        
        for(char c: s){
            auto temp = mySet.find(c);

            if(temp != mySet.end()){
                // std::cout << temp
                return c;
            }

            mySet.insert(c);
        }

        return 'w';
    }
};