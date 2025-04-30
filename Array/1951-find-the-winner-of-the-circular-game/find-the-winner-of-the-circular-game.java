class Solution {
    public int findTheWinner(int n, int k) {
        
        List<Integer> nums = new ArrayList<>();


        for(int i=1;i<=n;i++) {
            nums.add(i);
        }

        int curr = 0;

        while(nums.size() > 1) {
            curr += (k-1);
            int index = curr%(nums.size());            
            nums.remove(index); 
            curr=index;
        }

        return nums.get(0);
        
    }
}