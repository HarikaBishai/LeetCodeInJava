function twoSum(nums: number[], target: number): number[] {
    const seenSum: Record<number, number> = {};
    for(let i=0;i<nums.length; i++) {
        const rem = target-nums[i];
        if(rem in seenSum) {
            return [seenSum[rem], i];
            break;
        }
        seenSum[nums[i]] = i;
    }
    return [-1, -1];
};