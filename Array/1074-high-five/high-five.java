class Solution {
    public int[][] highFive(int[][] items) {


        Map <Integer, PriorityQueue<Integer>> map = new TreeMap<>();

        for(int[] item: items) {
            int id = item[0];
            int score = item[1];

            map.putIfAbsent(id, new PriorityQueue<>());

            Queue<Integer> pq = map.get(id);
            pq.offer(score);
            if(pq.size()>5) {
                pq.poll();
            }
            
        }

        int[][] out = new int[map.size()][2];
        int i = 0;
        for(int key: map.keySet()) {
           
            out[i][0] = key;
            Queue<Integer> pq = map.get(key);
            while(!pq.isEmpty()) {
                out[i][1]+=pq.poll();
            }
            
            out[i][1] /= 5;

            i++;
        }

        return out;
    }
}