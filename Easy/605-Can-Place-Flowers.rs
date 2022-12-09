// ou have a long flowerbed in which some of the plots are planted (1), and some are not (0).
// However, flowers cannot be planted in adjacent plots.

// Given an integer array flowerbed containing 0's and 1's, and an integer n,
// return if n new flowers can be planted in the flowerbed according to this no-adjacent-flowers rule.

impl Solution {
    pub fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
        // for counting every new flower planted
        let mut flower_counter: i32 = 0;

        // making a new array for edge cases
        let mut temp_array = Vec::new();
        let nn = [0];
        let nnn = [0];
        temp_array.extend_from_slice(&nn);
        temp_array.extend_from_slice(&flowerbed);
        temp_array.extend_from_slice(&nnn);

        // checking for three 0`s in a row with a pointer
        let mut pointer = 0;
        for pointer in 1..temp_array.len() - 1 {
            if temp_array[pointer - 1] == 0
                && temp_array[pointer] == 0
                && temp_array[pointer + 1] == 0
            {
                // planting one flower in the middle of this row + changing the counter
                temp_array[pointer] = 1;
                flower_counter += 1;
            }
        }

        flower_counter >= n
    }
}
