class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        // if(n==0)return true;
        // List<Integer> extended = new ArrayList<>();
        // extended.add(0);

        // for(int flower: flowerbed) {
        //     extended.add(flower);
        // }
        // extended.add(0);

        // for(int i=1; i<extended.size()-1; i++) {

        //     if (extended.get(i-1) == 0  && extended.get(i) == 0 && extended.get(i+1) == 0) {
        //         extended.set(i, 1);
        //         n-=1;
        //     }
        //     if(n==0) {
        //         return true;
        //     }
        // }
        // return false;

        if(n==0)return true;
        int fn = flowerbed.length;

        for(int i=0; i<fn; i++) {

            if ((i == 0 || flowerbed[i-1] == 0) && flowerbed[i] == 0 && (i==fn-1 || flowerbed[i+1] == 0)) {
                flowerbed[i] = 1;
                n-=1;
            }
            if(n==0) {
                return true;
            }
        }
        return false;

    }
}