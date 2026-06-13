class Solution {
    List<Integer> result = new ArrayList<>();
    public int[] restoreArray(int[][] adjacentPairs) {
        Map<Integer, List<Integer>> graph = new HashMap<>();

        for(int[] pair: adjacentPairs){
            int a = pair[0];
            int b = pair[1];

            graph.computeIfAbsent(a, k -> new ArrayList<>()).add(b);
            graph.computeIfAbsent(b, k -> new ArrayList<>()).add(a);
        }

        int start = 0;

        for (int node: graph.keySet()){
            if(graph.get(node).size() == 1) {
                start = node;
                break;
            }
        }

        Set<Integer> visited = new HashSet<>();

        dfs(start, graph, visited);
        int[] out = new int[result.size()];
        for(int i=0;i<result.size();i++) {
            out[i] = result.get(i);
        }
        return out;

    }

    public void dfs(int node, Map<Integer, List<Integer>> graph, Set<Integer> visited) {
        visited.add(node);
        result.add(node);

        for(int nei: graph.getOrDefault(node, new ArrayList<>())) {
            if (!visited.contains(nei)) {
                dfs(nei, graph, visited);
            }
        }
    }
}