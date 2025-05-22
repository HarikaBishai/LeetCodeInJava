// class Node {
//     public int key;
//     public int val;
//     public Node next = null;
//     public Node prev = null;
//     public Node(int key, int val)  {
//         this.key = key;
//         this.val = val;
//     }

//     public Node() {
//         this.key = -1;
//         this.val = -1;
       
//     }
// }

// class LRUCache {
//     private Map<Integer, Node> map;
//     private Node head;
//     private Node tail;
//     private int capacity;

//     public LRUCache(int capacity) {
//         this.map = new HashMap<>();
//         this.capacity = capacity;
//         this.head = new Node();
//         this.tail = new Node();
        
//         this.head.next = tail;
//         this.tail.prev = head;

//     }
    
//     public int get(int key) {
//         if(map.containsKey(key)) {
//             Node node = map.get(key);
//             this.remove(node);
//             this.insertLast(node);
//             return node.val;
//         } 
//         return -1;
//     }

//     public Node remove(Node node) {
//         Node prev = node.prev;
//         Node next = node.next;
//         prev.next = next;
//         next.prev = prev;
//         return node;
//     }

//     public void insertLast(Node node) {
//         Node prev = tail.prev;
//         prev.next = node;
//         node.prev = prev;
//         node.next = tail;
//         tail.prev = node;
//     }
    
//     public void put(int key, int value) {
//         Node newNode = new Node(key, value);
//         if(map.containsKey(key)) {
//             Node node = map.get(key);
//             remove(node);
//         } else {
//             if(map.size() + 1 > capacity) {
//                 Node node = remove(head.next); 
//                 map.remove(node.key);
//             } 
//         }
//         map.put(key, newNode);
//         insertLast(newNode);
//     }
// }


class LRUCache extends LinkedHashMap<Integer, Integer> {
    private final int capacity;

    public LRUCache(int capacity) {
        super(capacity, 0.75f, true);
        this.capacity = capacity;
    }

    public void put(int key, int value) {
        super.put(key,value);
    }

    public int get(int key) {
        return super.getOrDefault(key,-1);
    }
    @Override
    public boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
        return size() > capacity;
    }




}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */