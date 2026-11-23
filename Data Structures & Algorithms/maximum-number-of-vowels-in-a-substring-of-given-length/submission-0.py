class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        pass
        windows=s[:k]
        current_vowel=0
        for ch in windows:
            if ch in"aeiou":
                current_vowel+=1
        max_vowel=current_vowel
        left=0
        for right in range(k,len(s)):
            if s[left] in "aeiou":
                current_vowel-=1
            if s[right] in "aeiou":
                current_vowel+=1
            max_vowel=max(current_vowel,max_vowel)
            left+=1
        return max_vowel