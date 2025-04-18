class Solution {
    public int findKthLargest(int[] nums, int k) {

        Queue<Integer> pq = new PriorityQueue<>();

        for(int i=0;i<nums.length;i++) {
            pq.offer(nums[i]);

            if(i>=k){
                pq.poll();
            }
        }

        return pq.peek();
    }
}