/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int pairSum(ListNode head) {
        if(head == null) {
            return 0;
        }

        ListNode slow = head;
        ListNode fast = head;
        ListNode last = null;

        while(fast!=null && fast.next!=null) {
            last = slow;
            slow = slow.next;
            fast = fast.next.next;

        }

        
        ListNode prev = null;
        ListNode next = null;
        ListNode curr = slow;

        last.next = null;

        while(curr!=null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr= next;
        }

        int maxSum = 0;
        ListNode start = head;
        ListNode end = prev;
        while(end!=null && start!=null) {
            maxSum = Math.max(maxSum, end.val + start.val);
            end = end.next;
            start = start.next;
        }

        return maxSum;

    }
}