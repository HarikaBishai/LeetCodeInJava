class Solution {
    public int findTheWinner(int n, int k) {
        int winner = 0;

        for(int i=2;i<=n;i++) {
            winner = (winner+k)%i;
        }

        return winner+1;


        
        // List<Integer> nums = new ArrayList<>();

        // for(int i=1;i<=n;i++) {
        //     nums.add(i);
        // }

        // int curr = 0;

        // while(nums.size() > 1) {
        //     curr += (k-1);
        //     int index = curr%(nums.size());            
        //     nums.remove(index); 
        //     curr=index;
        // }

        // return nums.get(0);
        
    }
}