/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let curr_sum = -Infinity;
    let max_so_far = -Infinity;
    for(let num of nums) {
        curr_sum = Math.max(curr_sum + num, num)
        max_so_far = Math.max(curr_sum, max_so_far)
    }

    return max_so_far

};