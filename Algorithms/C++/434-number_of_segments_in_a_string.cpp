class Solution {
public:
    int countSegments(string s) {
        if (s == "") {
            return 0;
        }

        bool white = true;
        int count = 0;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] != ' ' && white) {
                count++;
                white = false;

            } else if (s[i] == ' ') {
                white = true;
            }
        }

        return count;
    }
};