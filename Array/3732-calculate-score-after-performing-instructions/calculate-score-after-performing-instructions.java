class Solution {



    public long calculateScore(String[] instructions, int[] values) {
        long score = 0;

        int idx = 0;
        int n = instructions.length;
        Set<Integer> visited= new HashSet<>();

        while(idx >= 0 && idx < n && !visited.contains(idx)) {
            visited.add(idx);
            if(instructions[idx].equals("jump")) {
                idx +=  (values[idx]);

            } else {
                score += (long)values[idx];
                idx++;

            }
            
        }
        return score;
    }
}