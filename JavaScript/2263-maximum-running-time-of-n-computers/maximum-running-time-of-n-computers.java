class Solution {

    public long maxRunTime(int n, int[] batteries) {
        
        long total = 0;

        for(int b: batteries) {
            total+= b;
        }

        long left = 0;
        long right = total/n;

        while(left < right) {
            long mid = (left+right+1)/2;

            if(canPower(n, mid,batteries)) {
                left = mid;
            } else {
                right = mid-1;
            }
        }
        return left;


    }

    public boolean canPower(int n, long time, int[] batteries) {
        long power = 0;

        for (int b: batteries) {
            power += Math.min(b, time);
        }

        return power >= n * time;
    }
}