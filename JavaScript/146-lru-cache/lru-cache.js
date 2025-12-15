class Node {
  constructor(key,value) {
    this.key = key;
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

var LRUCache = function(capacity) {
  this.capacity = capacity;
  this.map = new Map();
  this.head = new Node(null, null);
  this.tail = new Node(null, null);
  this.head.next = this.tail;
  this.tail.prev = this.head;
}

LRUCache.prototype.get = function(key) {
  if(!this.map.has(key)) return -1;
  
  const node = this.map.get(key);
  this.remove(node);
  this.insertAtFirst(node);
  return node.value;
}


LRUCache.prototype.put = function(key, value) {
  if(this.map.has(key)) {
    const node = this.map.get(key);
    node.value = value;
    this.remove(node);
    this.insertAtFirst(node);
    return;
  }
  const newNode = new Node(key, value);
  
  this.map.set(key, newNode);
  this.insertAtFirst(newNode);
  if(this.map.size > this.capacity) {
    const lru = this.tail.prev;
    this.remove(lru);
    this.map.delete(lru.key)
  }
}

LRUCache.prototype.remove = function(node) {
  node.prev.next = node.next;
  node.next.prev = node.prev;
}

LRUCache.prototype.insertAtFirst = function(node) {
  let next = this.head.next;
  node.prev = this.head;
  node.next = this.head.next;
  this.head.next = node;
  next.prev = node;
  
}
