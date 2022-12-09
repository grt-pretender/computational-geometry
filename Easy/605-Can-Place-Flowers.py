# ou have a long flowerbed in which some of the plots are planted (1), and some are not (0). 
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, and an integer n, 
# return if n new flowers can be planted in the flowerbed according to this no-adjacent-flowers rule.


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # for counting every new flower planted
        flower_counter = 0
        
        # making a new array for edge cases
        new_array = [0] + flowerbed + [0]

        # checking for three 0`s in a row with a pointer
        pointer = 0
        for pointer in range(1, len(new_array) - 1):
            if new_array[pointer - 1] == 0 and new_array[pointer] == 0 and new_array[pointer + 1] == 0:
        
        # planting one flower in the middle of this row + changing the counter
                new_array[pointer] = 1
                flower_counter += 1
        
        return flower_counter >= n



