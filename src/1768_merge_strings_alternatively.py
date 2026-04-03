class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        
        length, longer_word = (l1, word2) if l1 < l2 else (l2, word1)
        
        merged_word = ''
        for i in range(length):
            merged_word = merged_word + word1[i] + word2[i]

        return merged_word + longer_word[length:]

if __name__ == '__main__':
    r = Solution().mergeAlternately('john_doe', 'jane_doe')
    print(r)
