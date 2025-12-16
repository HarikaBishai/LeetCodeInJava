/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let numsSet = new Set(nums);
    let maxConsec = 0;
    for(let num of numsSet) {
       
        if(!numsSet.has(num-1)){
            let count = 1;
            let currNum = num;
            while(numsSet.has(currNum+1)) {
                count++;
                currNum++;
            }
            maxConsec = Math.max(maxConsec, count);
        }
    }
    return maxConsec;

};