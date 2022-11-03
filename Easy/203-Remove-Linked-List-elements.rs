// Given the head of a linked list and an integer val,
// remove all the nodes of the linked list that has Node.val == val, and return the new head.

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        // extra_node would be a new initial head -
        // in case of the actual head containing value to be removed
        let mut extra_node = Some(Box::new(ListNode { val: 0, next: head }));

        let mut previous = &mut extra_node;

        // iterate through the linked list
        while let Some(current_node) = &mut previous.as_mut().unwrap().next {
            // delete val by redirecting the pointer
            if current_node.val == val {
                previous.as_mut().unwrap().next = current_node.next.take();

            // continue iteration through the linked list
            } else {
                previous = &mut previous.as_mut().unwrap().next;
            }
        }

        // it always poimts to the actual head
        let answer = extra_node.unwrap().next;
        return answer;
    }
}
