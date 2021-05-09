class Solution:

    ## time complexity O(V+E) space complexity: O(V+E)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, queue = defaultdict(list), deque([])
        ind = {c: 0 for c in range(numCourses)}

        for end, start in prerequisites:
            ind[end] += 1
            graph[start].append(end)

        for key, value in ind.items():
            if value == 0:
                queue.append(key)

        ans = []
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            for course in graph[cur]:
                ind[course] -= 1
                if ind[course] == 0:
                    queue.append(course)

        return ans if len(ans) == numCourses else []

