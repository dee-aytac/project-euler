class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return len(s)
        longest_length = 1
        for i in range(len(s) - 1):
            seen = set()
            local_length = 0
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                elif s[j] not in seen:
                    local_length += 1
                seen.add(s[j])
            if local_length > longest_length:
                longest_length = local_length
        return longest_length


solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew"))