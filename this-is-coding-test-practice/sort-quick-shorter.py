# 파이썬의 장점을 살려 간결하게 작성한 퀵 정렬 소스코드
array = [7, 5, 9, 0, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 리스트의 원소가 하나 이하라면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    # 피벗보다 작은 요소만 담긴 리스트 (피벗을 포함)
    left_side = [x for x in tail if x <= pivot]
    # 피벗보다 큰 요소만 담긴 리스트
    right_side = [x for x in tail if x > pivot]
    # 분할 완료

    # 분할 이후 왼쪽과 오른쪽 리스트에 각각 퀵정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))