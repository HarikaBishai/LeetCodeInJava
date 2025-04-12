class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        

        // int maxValue = Arrays.stream(candies).max().orElse(0);

        int maxValue = 0;

        for(int num: candies) {
            if ( num > maxValue) {
                maxValue = num;
            }
        }

        List<Boolean> out = new ArrayList<>();
        for(int num: candies) {
            out.add(num+extraCandies >= maxValue);
            
        }

        return out;

    }
}