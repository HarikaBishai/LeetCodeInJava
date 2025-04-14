class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();


        for (String s: strs) {
            char[] sCharArray = s.toCharArray();
            Arrays.sort(sCharArray);

            String sortedS = new String(sCharArray);
            List<String> groupItems = map.getOrDefault(sortedS, new ArrayList<>());

            groupItems.add(s);

            map.put(sortedS, groupItems);
            
        }
        return new ArrayList<>(map.values());
    }
}