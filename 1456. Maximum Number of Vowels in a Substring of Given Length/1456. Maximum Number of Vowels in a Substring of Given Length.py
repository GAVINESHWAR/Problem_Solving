class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sub_str = s[:k]
        vowel = ['a','e','i','o','u']
        c=0
        for i in sub_str:
            if i in vowel:
                c+=1
        j = 0
        mc = c
        for i in range(k, len(s)):
            if s[i] in vowel:
                c+=1
            if s[i-k] in vowel:
                c-=1
            mc=max(mc,c)
        return mc