"""345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


Example 1:

Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"
Output: "leotcede"

 
Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        set_of_vowels = {
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U',
        }
        left = 0
        right = len(s) - 1
        
        l = list(s)  # noqa: E741
        
        while left < right:
            if l[left] in set_of_vowels and l[right] in set_of_vowels:
                # vowels swap
                l[left], l[right] = l[right], l[left]

                right -= 1
                left += 1
            
            left = left if l[left] in set_of_vowels else left + 1
            right = right if l[right] in set_of_vowels else right - 1

        return ''.join(l)

if __name__ == '__main__':
    s = Solution().reverseVowels('icecream')
    print(s)
