class Solution {
    public int[][] highFive(int[][] items) {

        Arrays.sort(items, (a,b) -> b[1]-a[1]);

        Map <Integer, List<Integer>> map = new TreeMap<>();

        for(int[] item: items) {
            int id = item[0];
            int score = item[1];

            List<Integer> studentScores = map.getOrDefault(id, new ArrayList<>());
            if(studentScores.size()<5) {
                studentScores.add(score);
                map.put(id, studentScores);
            }

            
        }

        int[][] out = new int[map.size()][2];
        int i = 0;
        for(int key: map.keySet()) {
            System.out.println(key);
            out[i][0] = key;
            out[i][1] = (map.get(key).stream().mapToInt(Integer::intValue).sum())/(map.get(key).size());
            i++;
        }

        return out;
    }
}