class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 1
        max_len = 0

        while right < len(s):
            

