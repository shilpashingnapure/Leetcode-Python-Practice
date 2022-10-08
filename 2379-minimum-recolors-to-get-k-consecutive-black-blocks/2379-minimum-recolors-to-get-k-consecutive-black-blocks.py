class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = j = 0
        whiteBlock = 0
        ans = 99999999
        while j < len(blocks):
            if blocks[j] == "W":
                whiteBlock += 1
            if j < k-1:
                j += 1
            elif j - i + 1 == k:
                ans = min(ans , whiteBlock)
                if blocks[i] == "W":
                    whiteBlock -= 1
                
                i += 1
                j += 1
        return ans
        