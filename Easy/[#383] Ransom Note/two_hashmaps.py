class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Freq = defaultdict(int)
        for i in ransomNote:
            Freq[i]+=1
        Freq2 = defaultdict(int)
        for i in magazine:
            Freq2[i]+=1
        for i in ransomNote:
            if Freq[i]>Freq2[i]:
                return False
        return True