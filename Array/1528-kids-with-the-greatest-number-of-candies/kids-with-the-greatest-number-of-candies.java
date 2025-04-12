class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        

        int maxValue = Arrays.stream(candies).max().orElse(0);

        List<Boolean> out = new ArrayList<>();
        for(int num: candies) {
            if (num+extraCandies >= maxValue) {
                out.add(true);
            } else {
                out.add(false);
            }
        }

        return out;

    }
}