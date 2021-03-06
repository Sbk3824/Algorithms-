'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, start, dict = 0, 0 , {}
        for i, ch in enumerate(s):
            if ch in dict:
                res = max(res, i - start)
                start = max(start, dict[ch]+1)
            dict[ch] = i;
        return max(res, len(s)-start)
