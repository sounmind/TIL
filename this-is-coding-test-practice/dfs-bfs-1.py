def dfs(x, y):
    # 주어진 리스트 범위를 벗어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 위치를 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 위치의 노드들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())

# 2차원 리스트(m * n)의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 음료 채우기
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            # 연결되어 있는 공간이면 result에 +1만 된다
            result += 1

print(result)


# 입력 예시
# 4 5
# 00110
# 00011
# 11111
# 00000

# 출력 예시
# 3