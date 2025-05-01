class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> out = new ArrayList<>();

        Map<String, List<String>> map = new HashMap<>();

        for(String s: strs) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String sortedString = new String(charArray);
            map.putIfAbsent(sortedString, new ArrayList<>());
            List<String> group = map.get(sortedString);
            group.add(s);
        }

        // for(List<String> group: map.values()) {
        //     out.add(group);
        // }
        return new ArrayList<>(map.values());


    }
}