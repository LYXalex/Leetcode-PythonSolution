class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        t,i =1,0
        while i < len(digits):
            t += digits[i]
            digits[i] = t%10
            t = t//10
            i+=1
        if t: digits.append(t)
        return digits[::-1]