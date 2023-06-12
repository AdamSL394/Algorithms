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
import java.util.HashSet;

class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        HashSet<Integer> dups = new HashSet<Integer>();
        ListNode previous = null;
        ListNode current = head;
        while (current != null){
            if (dups.contains(current.val)){
                previous.next = current.next;
            }else {
            dups.add(current.val);
            previous = current;
            }
            current = current.next;
        }

        return head;
    }
}