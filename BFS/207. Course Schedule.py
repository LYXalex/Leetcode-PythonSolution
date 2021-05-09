class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pres, Z = defaultdict(list), deque([])
        degrees = {c: 0 for c in range(numCourses)}

        for end, start in prerequisites:
            degrees[end] += 1
            pres[start].append(end)

        for key, value in degrees.items():
            if value == 0:
                Z.append(key)

        cnt = 0
        while Z:
            cur = Z.popleft()
            cnt += 1
            for course in pres[cur]:
                degrees[course] -= 1
                if degrees[course] == 0:
                    Z.append(course)

        return cnt == numCourses




