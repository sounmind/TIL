# 퀵 정렬
array = [7, 5, 9, 0, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗(기준 데이터)은 첫 번째 원소

    # 탐색을 시작하는 (피벗 다음) 왼쪽 끝 원소,
    # 탐색이 끝나면 피벗보다 큰 데이터의 인덱스를 저장된다.
    left = start + 1

    # 탐색이 끝나면 피벗보다 작은 데이터의 인덱스가 저장된다.
    right = end
    while left <= right:  # 왼쪽 끝 원소가 오른쪽 끝 원소보다 작거나 같을 때 반복
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
            print("분할!", end=" ")
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
        print(array)
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)

# 출력 결과
# [7, 5, 4, 0, 1, 6, 2, 9, 8]
# 분할! [2, 5, 4, 0, 1, 6, 7, 9, 8]
# [2, 1, 4, 0, 5, 6, 7, 9, 8]
# [2, 1, 0, 4, 5, 6, 7, 9, 8]
# 분할! [0, 1, 2, 4, 5, 6, 7, 9, 8]
# 분할! [0, 1, 2, 4, 5, 6, 7, 9, 8]
# 분할! [0, 1, 2, 4, 5, 6, 7, 9, 8]
# 분할! [0, 1, 2, 4, 5, 6, 7, 9, 8]
# 분할! [0, 1, 2, 4, 5, 6, 7, 8, 9]