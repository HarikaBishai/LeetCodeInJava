class Solution {
    public boolean closeStrings(String word1, String word2) {
        // should be of same length
        if(word1.length()!=word2.length()) {
            return false;
        }

        // should have the same character 

        Map<Character, Integer> map1 = new HashMap<>();
        for(char c: word1.toCharArray()) {
            map1.put(c, map1.getOrDefault(c, 0)+1);
        }

        Map<Character, Integer> map2 = new HashMap<>();
        for(char c: word2.toCharArray()) {
            map2.put(c, map2.getOrDefault(c, 0)+1);
        }

        if(!map1.keySet().equals(map2.keySet())) {
            return false;
        }

        // sort order of the values

        List<Integer> arr1 = new ArrayList<>(map1.values());
        List<Integer> arr2 = new ArrayList<>(map2.values());

        Collections.sort(arr1);
        Collections.sort(arr2);

        return arr1.equals(arr2);



    }
}