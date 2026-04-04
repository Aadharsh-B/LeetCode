"""605. Can Place Flowers.

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
class Solution:
    def canPlaceFlowers(self, flowerbeds: list[int], n: int) -> bool:
        is_previous_planted = 0
        is_plantable = 0

        for i in range(len(flowerbeds)):
            try:
                if flowerbeds[i + 1] == 0 and is_previous_planted == 0 and flowerbeds[i] == 0:
                    is_plantable += 1
                    is_previous_planted = 1
                else:
                    is_previous_planted = flowerbeds[i]
            except IndexError:
                # error occurs at terminus
                if is_previous_planted == 0 and flowerbeds[i] == 0:
                    is_plantable += 1
                
        return is_plantable >= n

if __name__ == '__main__':
    s = Solution().canPlaceFlowers([1,0,0,0,1], 2)
    print(s)
