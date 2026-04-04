class Solution:
    def test_divisibility(self, divisor: str, dividend: str) -> bool:
        q = len(dividend) // len(divisor)
        if len(dividend) % len(divisor) == 0 and (q * divisor) == dividend:
            return True
        return False

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ''

        r = ''
        short_word = str1 if len(str1) < len(str2) else str2
        for alphabet in short_word:
            r += alphabet
            if self.test_divisibility(r, str1) and self.test_divisibility(r, str2):
                gcd = r
            
        return gcd
                
            

if __name__ == '__main__':
    s = Solution().gcdOfStrings('ABAB', 'AB')
    print(s)
