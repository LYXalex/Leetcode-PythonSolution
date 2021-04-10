class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        preorder = preorder.split(',')
        i = 0
        slots = 1
        for node in preorder:
            if slots == 0:
                return False

            if node != '#':
                slots += 1
            else:
                slots -= 1

        return slots == 0




