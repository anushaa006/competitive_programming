class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_w = sum(1 for b in blocks[:k] if b == 'W') 
        min_recolors = count_w 
        
        for i in range(1, len(blocks) - k + 1):
            count_w += (blocks[i + k - 1] == 'W') - (blocks[i - 1] == 'W')
            min_recolors = min(min_recolors, count_w)
        
        return min_recolors
