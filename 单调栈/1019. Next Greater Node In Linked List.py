# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        stack, ans = [], [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if stack: ans[i] = stack[-1]
            stack.append(nums[i])
        return ans

