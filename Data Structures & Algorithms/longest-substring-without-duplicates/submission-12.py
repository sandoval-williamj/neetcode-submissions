class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        char_index = {}
        max_substring = 1
        count = 0
        w1 = 0
        clear_i = -1
        l = len(s)

        while w1 < l:
            if s[w1] in char_index and char_index[s[w1]] > clear_i:
                count = w1 - clear_i - 1
                max_substring = max(max_substring, count)
                clear_i = char_index[s[w1]]

            char_index[s[w1]] = w1
            w1 = w1 + 1

        count = w1 - clear_i - 1
        max_substring = max(max_substring, count)

        return max_substring
