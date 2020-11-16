# 선택 정렬 교재 예시

array = [7, 5, 9, 0, 1, 6, 2, 4, 8]
# i번째 요소를 그 이후 요소의 최솟값과 교체한다.
for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):  # 나머지 요소 중 최솟값 찾기
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 값 서로 바꾸기
    print(array)

# 실행결과
# [0, 5, 9, 7, 1, 6, 2, 4, 8]
# [0, 1, 9, 7, 5, 6, 2, 4, 8]
# [0, 1, 2, 7, 5, 6, 9, 4, 8]
# [0, 1, 2, 4, 5, 6, 9, 7, 8]
# [0, 1, 2, 4, 5, 6, 9, 7, 8]
# [0, 1, 2, 4, 5, 6, 9, 7, 8]
# [0, 1, 2, 4, 5, 6, 7, 9, 8]
# [0, 1, 2, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 4, 5, 6, 7, 8, 9]
