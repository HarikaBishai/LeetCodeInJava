class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if(n==0)return true;
        List<Integer> extended = new ArrayList<>();
        extended.add(0);

        for(int flower: flowerbed) {
            extended.add(flower);
        }
        extended.add(0);

        for(int i=1; i<extended.size()-1; i++) {
            int first = extended.get(i-1);
            int curr = extended.get(i);
            int last = extended.get(i+1);

            if (first == 0  && curr == 0 && last == 0) {
                extended.set(i, 1);
                n-=1;
            }
            System.out.println(n);
            if(n==0) {
                return true;
            }
            System.out.println(n);
        }
        return false;
    }
}