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


    let dummy = new ListNode(0);
    let tail = dummy;

    while(list1 && list2){
        if(list1 && list2) {
            if(list1.val < list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next =  list2;
                list2 = list2.next;
            }
        }
        tail = tail.next;
    }
    tail.next = list1 || list2;
    return dummy.next;
}
var mergeKLists = function(lists) {
    if(!lists || lists.length == 0) return null;

    function helper(left, right) {
        if (left > right) return null;
        if(left == right) return lists[left];
        let mid = Math.floor((left+right)/2);
        let l1 = helper(left, mid);
        let l2 = helper(mid+1, right);
        return mergeLists(l1, l2)
        
    }
    // while(lists.length > 1) {
    //     if(lists.length == 2) {
    //         lists = [mergeLists(lists[0], lists[1])];
    //     } else {
    //         let mid = Math.floor(lists.length/2);
    //         lists = [mergeKLists(lists.slice(0, mid)), mergeKLists(lists.slice(mid, lists.length))];

    //     }

    // }

    return helper(0, lists.length-1);
};