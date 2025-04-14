class SmallestInfiniteSet {


    private int next;
    private Set<Integer> inHeap;
    private Queue<Integer> minHeap;
    public SmallestInfiniteSet() {
        next = 1;
        inHeap = new HashSet<>();
        minHeap = new PriorityQueue<>();
    }
    
    public int popSmallest() {
        if(!minHeap.isEmpty()) {
            int smallest = minHeap.poll();
            inHeap.remove(smallest);
            return smallest;
        }
        return next++;
    }
    
    public void addBack(int num) {

        if(num<next && !inHeap.contains(num)) {
            inHeap.add(num);
            minHeap.offer(num);
        }
        
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */