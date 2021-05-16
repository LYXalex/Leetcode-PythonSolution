class Solution:
    def minJumps(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return 0
        stack, visited, step = [0], {0}, 0
        valDic = defaultdict(list)
        for i, val in enumerate(arr):
            valDic[val].append(i)

        while stack:
            next = []
            for index in stack:
                if index == len(arr) - 1:
                    return step

                for child in valDic[arr[index]]:
                    if child not in visited:
                        visited.add(child)
                        next.append(child)

                for child in [index - 1, index + 1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        next.append(child)

                valDic[arr[index]].clear()

            stack = next
            step += 1
        return step


