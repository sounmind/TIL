# 삽입 정렬
array = [7, 5, 9, 0, 1, 6, 2, 4, 8]

# i번째 요소를 그 이전의 모든 요소와 비교하여 작으면 교체하고, 크면 그대로 둔다.
for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 1씩 감소
        if array[j] < array[j - 1]:  # j번째 요소가 그 이전 요소보다 작다면
            array[j], array[j - 1] = array[j - 1], array[j]  # 서로 교체
            print(i, array)
        else:  # 작지 않다면 그대로 두고 다음 요소로 넘어감
            break

# 출력 결과 (교체될 때만)
# 1 [5, 7, 9, 0, 1, 6, 2, 4, 8]
# 3 [5, 7, 0, 9, 1, 6, 2, 4, 8]
# 3 [5, 0, 7, 9, 1, 6, 2, 4, 8]
# 3 [0, 5, 7, 9, 1, 6, 2, 4, 8]
# 4 [0, 5, 7, 1, 9, 6, 2, 4, 8]
# 4 [0, 5, 1, 7, 9, 6, 2, 4, 8]
# 4 [0, 1, 5, 7, 9, 6, 2, 4, 8]
# 5 [0, 1, 5, 7, 6, 9, 2, 4, 8]
# 5 [0, 1, 5, 6, 7, 9, 2, 4, 8]
# 6 [0, 1, 5, 6, 7, 2, 9, 4, 8]
# 6 [0, 1, 5, 6, 2, 7, 9, 4, 8]
# 6 [0, 1, 5, 2, 6, 7, 9, 4, 8]
# 6 [0, 1, 2, 5, 6, 7, 9, 4, 8]
# 7 [0, 1, 2, 5, 6, 7, 4, 9, 8]
# 7 [0, 1, 2, 5, 6, 4, 7, 9, 8]
# 7 [0, 1, 2, 5, 4, 6, 7, 9, 8]
# 7 [0, 1, 2, 4, 5, 6, 7, 9, 8]
# 8 [0, 1, 2, 4, 5, 6, 7, 8, 9]