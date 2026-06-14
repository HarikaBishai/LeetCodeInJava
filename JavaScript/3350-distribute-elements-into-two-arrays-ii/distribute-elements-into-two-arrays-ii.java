class Solution {
    public int[] resultArray(int[] nums) {
        int n = nums.length;

        int[] sorted = nums.clone();
        Arrays.sort(sorted);

        Map<Integer, Integer> rank = new HashMap<>();

        int r = 1;
        for(int num: sorted) {
            if(!rank.containsKey(num)){
                rank.put(num, r);
                r++;
            }
        }

        List<Integer> arr1 = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();

        Fenwick bit1 = new Fenwick(r+2);
        Fenwick bit2 = new Fenwick(r+2);
        arr1.add(nums[0]);
        bit1.add(rank.get(nums[0]), 1);
        arr2.add(nums[1]);
        bit2.add(rank.get(nums[1]), 1);

        for(int i=2; i<nums.length;i++) {
            int val = nums[i];
            int idx = rank.get(val);
            int greaterCountArr1 = arr1.size() - bit1.sum(idx);
            int greaterCountArr2 = arr2.size() - bit2.sum(idx);

            if(greaterCountArr1 > greaterCountArr2) {
                arr1.add(val);
                bit1.add(idx, 1);
            } else if(greaterCountArr1 < greaterCountArr2) {
                arr2.add(val);
                bit2.add(idx, 1);
            } else {
                if(arr1.size() <= arr2.size()) {
                    arr1.add(val);
                    bit1.add(idx, 1);
                } else {
                    arr2.add(val);
                    bit2.add(idx, 1);
                }
            }
        }

        int[] out = new int[n];
        int i=0;
        for (int num: arr1) {
            out[i++] = num;
        }
        for (int num: arr2) {
            out[i++] = num;
        }
        return out;
    }
}


class Fenwick {
    int[] tree;

    Fenwick(int n) {
        tree = new int[n];
    }

    public void add(int index, int value) {
        while(index < tree.length) {
            tree[index] += value;
            index += index & -index;
        }
    }



    public int sum(int index) {
        int out = 0;
        while(index > 0){
            out += tree[index];
            index -= index & -index;
        }
        return out;
    }
}