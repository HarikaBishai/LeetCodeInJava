class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        if(n==0) {
            return 0;
        }
        int out = 0;

        int rightMax = prices[n-1];

        for(int i=n-2; i >=0;i--) {
            rightMax = Math.max(rightMax, prices[i]);
            out = Math.max(out, rightMax - prices[i]);
        }
        return out;

    }
}