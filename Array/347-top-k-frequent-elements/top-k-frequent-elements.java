class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for(int num: nums) {
            map.put(num, map.getOrDefault(num, 0)+1);
        }

        Queue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        for(Integer key: map.keySet()) {
            int[] curr = {map.get(key), key};
        

            pq.offer(curr);

            if(pq.size() > k) {
                pq.poll();
            }
        }

        int[] out = new int[pq.size()];
        int i=0;
        while(!pq.isEmpty()) {
            out[i] = pq.poll()[1];
            i++;
        }
        return out;


    }
}