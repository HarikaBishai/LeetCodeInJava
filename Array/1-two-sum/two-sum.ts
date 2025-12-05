function twoSum(nums: number[], target: number): number[] {
    const seenSum: Record<number, number> = {};
    let out: [number, number] = [-1, -1]
    for(let i in nums) {
        const rem = target-nums[i];
        if(rem in seenSum) {
            out = [seenSum[rem], Number(i)];
            break;
        }
        seenSum[nums[i]] = Number(i);
    }
    return out;
};