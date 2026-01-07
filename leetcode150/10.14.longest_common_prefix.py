from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Scan character by character across all strings until a mismatch
        min_word_len = min(len(s) for s in strs)
        common_prefix = ""

        for i in range(min_word_len):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return common_prefix

            common_prefix += char

        return common_prefix