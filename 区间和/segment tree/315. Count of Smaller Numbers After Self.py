# class Node:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end
#         self.sum = 0
#         self.left = None
#         self.right = None

# class segmentTree:

#     def __init__(self,nums):
#         self.nums = nums
#         self.root = self.build(nums,0,len(nums)-1)


#     def build(self,nums,l,r):
#         if l > r:
#             return None
#         # leaf node
#         if l == r:
#             node = Node(l,r)
#             node.sum = nums[l]
#             return node
#         mid = l + (r-l)//2
#         root = Node(l,r)
#         root.left = self.build(nums,l,mid)
#         root.right = self.build(nums,mid+1,r)

#         root.sum = root.left.sum + root.right.sum

#         return root

#     def update(self,node,index,val):
#         # leaf node
#         if node.start == node.end:
#             node.sum = val
#             return
#         else:
#             mid = node.start + (node.end-node.start)//2
#             if index <= mid:
#                 self.update(node.left,index,val)
#             else:
#                 self.update(node.right,index,val)
#             node.sum = node.left.sum + node.right.sum


#     def rangeSum(self,node,left,right):
#         if node.start == left and node.end == right:
#             return node.sum

#         mid = node.start + (node.end - node.start)//2
#         if right <= mid: return self.rangeSum(node.left,left,right)
#         elif left > mid: return self.rangeSum(node.right,left,right)
#         else: return self.rangeSum(node.left,left,mid) + self.rangeSum(node.right,mid+1,right)


# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         if not nums: return []
#         nums = [num+10001 for num in nums]
#         number = [0] * 20002
#         st = segmentTree([0]*20002)
#         n = len(nums)
#         number[nums[n-1]] +=1
#         st.update(st.root,nums[n-1],number[nums[n-1]])
#         res = []
#         res.append(0)
#         for i in range(n-2,-1,-1):
#             number[nums[i]] += 1
#             st.update(st.root,nums[i],number[nums[i]])
#             res.insert(0,st.rangeSum(st.root,0,nums[i]-1))
#         return res
class Node:
    def __init__(self, low, high):
        self.count = 0
        self.low = low
        self.high = high
        self.mid = (low + high) // 2
        self.left = None
        self.right = None


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def init_tree(low, high):
            if low == high:
                return Node(low, high)
            if low > high:
                return None
            node = Node(low, high)
            node.left, node.right = init_tree(low, node.mid), init_tree(node.mid + 1, high)
            return node

        def add(node, target_val):
            if not node:
                return
            node.count += 1
            if target_val <= node.mid:
                add(node.left, target_val)
            else:
                add(node.right, target_val)
            return

        def query(node, range_low, range_high):
            if range_low > range_high:
                return 0
            if not node:
                return 0
            if range_low == node.low and range_high == node.high:
                return node.count
            if range_high <= node.mid:
                return query(node.left, range_low, range_high)
            elif node.mid + 1 <= range_low:
                return query(node.right, range_low, range_high)
            # the range is across the two childs
            else:
                return query(node.left, range_low, node.mid) + query(node.right, node.mid + 1, range_high)

        minimum = -1e4 - 1
        maximum = 1e4 + 1
        root = init_tree(minimum, maximum)
        answer = []
        for val in reversed(nums):
            add(root, val)
            answer.append(query(root, minimum, val - 1))
        return reversed(answer)