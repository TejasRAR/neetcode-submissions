class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0                          # l is not bound by any upper range like length of s, voh apna apna mast hai, he's used/incremented to just calculate the length of the substring
        res= 0 
        hashSet = set()

        for r in range(len(s)):        # Iterates over the indices of s 
            while s[r] in hashSet:     # Checks if the element/letter is also present in hashset 
                hashSet.remove(s[l])
                l += 1

            hashSet.add(s[r])
            res = max(res, r - l + 1)

        return res