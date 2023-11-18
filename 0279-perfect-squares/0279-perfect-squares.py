class Solution:
    def numSquares(self, n: int) -> int:
        if(n == 1):
            return 1
        squares = []
        for i in range(1, n):
            sq = i*i
            if sq > n:
                break
            squares.append(sq)
        q = deque()
        visited = set([n])
        q.append((n, 0))

        while q:
            cur, steps = q.popleft()

            for square in squares:
                leftover = cur - square
                step = steps + 1
                if(leftover == 0):
                    return step
                if(leftover > 0 and leftover not in visited):
                    visited.add(leftover)
                    q.append((leftover, step))

