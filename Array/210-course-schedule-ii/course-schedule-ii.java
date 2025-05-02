class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        

        Map<Integer, List<Integer>> graph = new HashMap<>();
        Map<Integer, Integer> indegree = new HashMap<>();

        for(int i=0;i<numCourses;i++) {
            indegree.put(i, 0);
        }


        for(int[] prereq: prerequisites) {
            int v = prereq[0];
            int u = prereq[1];

            graph.putIfAbsent(u, new ArrayList<>());
            List<Integer> nodes = graph.get(u);

            nodes.add(v);
            indegree.put(v, indegree.get(v)+1);
        }

        Queue<Integer>q = new LinkedList<>();

        for(int key: indegree.keySet()) {
            if(indegree.get(key) == 0) {
                q.offer(key);
            }
        }



        List<Integer> out = new ArrayList<>();

        while(!q.isEmpty()) {
            int node = q.poll();

            out.add(node);

            List<Integer> neighbours = graph.getOrDefault(node, new ArrayList<>());

            for(int nei: neighbours) {
                indegree.put(nei, indegree.get(nei)-1);
                if(indegree.get(nei) == 0) {
                    q.offer(nei);
                }
            }
            
        }


        return (out.size() != numCourses) ? new int[]{} 
            : out.stream().mapToInt(Integer::intValue).toArray();

    }
}