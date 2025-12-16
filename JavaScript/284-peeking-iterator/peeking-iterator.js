/**
 * // This is the Iterator's API interface.
 * // You should not implement it, or speculate about its implementation.
 * function Iterator() {
 *    @ return {number}
 *    this.next = function() { // return the next number of the iterator
 *       ...
 *    }; 
 *
 *    @return {boolean}
 *    this.hasNext = function() { // return true if it still has numbers
 *       ...
 *    };
 * };
 */

/**
 * @param {Iterator} iterator
 */
var PeekingIterator = function(iterator) {
    this.iterator = iterator;
    this.peeked = null;
    this.hasPeeked = false;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.peek = function() {
    if(!this.hasPeeked) {
        this.peeked = this.iterator.next();
        this.hasPeeked = true;
    }
    return this.peeked;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.next = function() {
    if(this.hasPeeked) {
        const value = this.peeked;
        this.peeked = null;
        this.hasPeeked = false;
        return value;
    }
    return this.iterator.next();
};

/**
 * @return {boolean}
 */
PeekingIterator.prototype.hasNext = function() {
    return this.hasPeeked || this.iterator.hasNext();
};

/** 
 * Your PeekingIterator object will be instantiated and called as such:
 * var obj = new PeekingIterator(arr)
 * var param_1 = obj.peek()
 * var param_2 = obj.next()
 * var param_3 = obj.hasNext()
 */