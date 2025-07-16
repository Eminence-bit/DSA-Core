class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Freq = defaultdict(int)
        for i in range(len(ransomNote)):
            Freq[ransomNote[i]]+=1
        Freq2 = defaultdict(int)
        for i in range(len(magazine)):
            Freq2[magazine[i]]+=1
        for i in range(len(ransomNote)):
            if Freq[ransomNote[i]]>Freq2[ransomNote[i]]:
                return False
        return True