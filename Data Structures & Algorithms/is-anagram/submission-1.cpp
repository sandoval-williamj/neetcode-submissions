using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int s_length = s.size(), t_length = t.size();

        if (s_length != t_length) {
            return false;
        }

        unordered_map<char, int> s_dict;
        unordered_map<char, int> t_dict;

        for (int i = 0; i < s_length; i++) {
            s_dict[s[i]]++;
            t_dict[t[i]]++;
        }

        for (auto& pair : s_dict) {
            char key = pair.first;
            int value = pair.second;

            if (t_dict[key] != value) {
                return false;
            }
        }

        return true;
    }
};
