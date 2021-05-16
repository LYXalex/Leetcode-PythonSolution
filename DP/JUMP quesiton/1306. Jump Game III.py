class Solution:

    # iterative
    def canReach1(self, arr: List[int], start: int) -> bool:
        self.ans = False
        stack, visited = [start], set()
        visited.add(start)
        if arr[start] == 0:
            return True
        while stack:
            cur = stack.pop()
            if cur + arr[cur] < len(arr) and cur + arr[cur] not in visited:
                if arr[cur + arr[cur]] == 0:
                    return True
                visited.add(cur + arr[cur])
                stack.append(cur + arr[cur])
            if cur - arr[cur] >= 0 and cur - arr[cur] not in visited:
                if arr[cur - arr[cur]] == 0:
                    return True
                visited.add(cur - arr[cur])
                stack.append(cur - arr[cur])
        return False

    # recursive
    def canReach(self, arr: List[int], start: int) -> bool:

        def dfs(arr, cur):
            if 0 <= cur < len(arr) and arr[cur] >= 0:
                arr[cur] = -arr[cur]

                return arr[cur] == 0 or dfs(arr, cur + arr[cur]) or dfs(arr, cur - arr[cur])
            return False

        return dfs(arr, start)






