class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();

        for(int num: arr) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }



        return map.values().size() == new HashSet<>(map.values()).size();

        // Set<Integer> set = new HashSet<>();

        // for(int value: map.values()) {
        //     if(set.contains(value)) {
        //         return false;
        //     }
        //     set.add(value);
        // }


        // return true;
        
    }
}