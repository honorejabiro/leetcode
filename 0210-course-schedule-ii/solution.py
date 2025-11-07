class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        in_degree = {a: 0 for a in range(numCourses)}
        neighbors = defaultdict(set)

        for u, v in prerequisites:
            in_degree[u] += 1
            neighbors[v].add(u)

        q = deque([x for x in in_degree if in_degree[x] == 0])
        scheduled = []

        while q:

            curr = q.popleft()
            scheduled.append(curr)

            for dst in neighbors[curr]:
                in_degree[dst] -= 1

                if in_degree[dst] == 0:
                    q.append(dst)

        return scheduled if len(scheduled) == numCourses else []
