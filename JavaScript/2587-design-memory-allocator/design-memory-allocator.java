class Allocator {
    private int[] memory;
    private int n;

    public Allocator(int n) {
        memory = new int[n];
        this.n = n;
    }
    
    public int allocate(int size, int mID) {
        int count = 0;
        int idx = -1;

        for (int i=0;i<n;i++){
            if(memory[i] == 0) {
                count++;
            } else {
                count = 0;
            }
            if(count == size) {
                idx = i-size+1;
                break;
            }
        }
        if(idx!=-1) {
            for (int i=idx; i<idx+size;i++){
                memory[i] = mID;
            }
        }
       
        return idx;
    }
    
    public int freeMemory(int mID) {
        int freed = 0;
        for(int i=0;i<n;i++) {
            if(memory[i] == mID) {
                freed++;
                memory[i] = 0;
            }
        }
        return freed;
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator obj = new Allocator(n);
 * int param_1 = obj.allocate(size,mID);
 * int param_2 = obj.freeMemory(mID);
 */