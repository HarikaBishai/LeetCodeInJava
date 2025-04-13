class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        // List<List<Integer>> out = new ArrayList<>();

        // Set<Integer> set1 = Arrays.stream(nums1).boxed().collect(Collectors.toSet());
        // Set<Integer> set2 = Arrays.stream(nums2).boxed().collect(Collectors.toSet());

        // Set<Integer> diff1 = new HashSet<>(set1);
        // diff1.removeAll(set2);

        // Set<Integer> diff2 = new HashSet<>(set2);
        // diff2.removeAll(set1);

        // out.add(new ArrayList(diff1));
        // out.add(new ArrayList(diff2));

        // return out; 

        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();

        for (int num: nums1) set1.add(num);
        for (int num: nums2) set2.add(num);

        for(int num: nums2) {
            if (set1.contains(num)) {
                set1.remove(num);
            }
        }

        for(int num: nums1) {
            if (set2.contains(num)) {
                set2.remove(num);
            }
        }

        List<List<Integer>> out = new ArrayList<>();
        out.add(new ArrayList<>(set1));
        out.add(new ArrayList<>(set2));
        return out;









    }
}