class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        Stack<List<Integer>> stk = new Stack<>();

        for(int[] interval: intervals) {
            if(stk.isEmpty() || stk.peek().get(1) < interval[0]) {
                List<Integer> curr = Arrays.stream(interval).boxed().collect(Collectors.toList());
                stk.push(curr);
            }
            else {
                List<Integer> last = stk.pop();
                List<Integer> curr = new ArrayList();

                curr.add(last.get(0));
                curr.add(Math.max(last.get(1), interval[1]));

                stk.push(curr);
            }
        }

        int[][] out = new int[stk.size()][2];
        int i = stk.size()-1; 
        while(!stk.isEmpty()) {
            List<Integer> curr = stk.pop();
            out[i--] = curr.stream().mapToInt(Integer::intValue).toArray();
        }

        return out;



    }
}