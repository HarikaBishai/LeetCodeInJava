class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;

        int[][] pairs = new int[n][2];

        for(int i=0;i<n;i++) {
            pairs[i][0] = nums2[i];
            pairs[i][1] = nums1[i];
        }


        Arrays.sort(pairs, (a,b) -> b[0]-a[0]);

        Queue<Integer> q = new PriorityQueue<>();
        long out = 0;
        long sum = 0;
        for(int i=0;i<n;i++) {
            int num1 = pairs[i][1];
            int num2 = pairs[i][0];

            q.offer(num1);
            sum+=num1;

            if(q.size()>k) {
                sum-=q.poll();
            }

            if(q.size()==k) {
                out = Math.max(out, (long)sum*num2);
            }
            
        }
        return out;
    }
}