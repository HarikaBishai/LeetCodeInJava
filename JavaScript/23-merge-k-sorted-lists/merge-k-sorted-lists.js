/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */

function mergeLists(list1, list2) {
    let l1 = list1;
    let l2 = list2;

    let dummy = new ListNode(0);
    let result = dummy;

    while(l1||l2){
        if(l1 && l2) {
            if(l1.val < l2.val) {
                result.next = new ListNode(l1.val);
                l1 = l1.next;
            } else {
                result.next =  new ListNode(l2.val);
                l2 = l2.next;
            }
        } else if(l1) {
            result.next =  new ListNode(l1.val);
            l1 = l1.next;
        } else {
            result.next =  new ListNode(l2.val);
            l2 = l2.next;
        }
        result = result.next;
    }
    console.log(dummy)
    return dummy.next;
}
var mergeKLists = function(lists) {
    if (!lists.length) return null;
    while(lists.length > 1) {
        if(lists.length == 2) {
            lists = [mergeLists(lists[0], lists[1])];
        } else {
            let mid = Math.floor(lists.length/2);
            lists = [mergeKLists(lists.slice(0, mid)), mergeKLists(lists.slice(mid, lists.length))];

        }

    }
    return lists[0];
};