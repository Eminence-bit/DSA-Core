class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = defaultdict(int)
        for c in magazine:
            freq[c]+=1
        for c in ransomNote:
            freq[c]-=1
            if freq[c]<0:
                return False
        return True