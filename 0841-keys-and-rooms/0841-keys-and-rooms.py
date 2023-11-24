class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(node: int):

            visited.add(node)

            neighbors = rooms[node]

            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor) 


        dfs(0)

        return len(visited) == len(rooms)
