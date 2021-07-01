class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if not x[0].isdigit(): return False
        n = len(x)
        if n ==1 : return True
        if n % 2 == 0:
            left,right = x[:n//2], x[n//2:]
        else:
            left,right = x[:n//2],x[n//2+1:]
        return left == right[::-1]