#include <stdio.h>

int BSearch(int array[], int len, int target)
{
    int first = 0;      // 탐색 대상의 시작 인덱스 값
    int last = len - 1; // 탐색 대상의 마지막 인덱스 값
    int mid;

    while (first <= last) // 배열의 처음이 마지막 보다 작거나 같을 때
    {
        mid = (first + last) / 2; // 탐색 대상의 중앙을 찾는다
        if (target == array[mid]) // 중앙에 저장된 것이 타겟이라면
        {
            return mid; // 탐색 완료!
        }
        else // 타겟이 아니라면 탐색 대상을 반으로 줄이기
        {
            if (target < array[mid])
                last = mid - 1; // 왜 -1을 하였을까? -> 타겟이 중앙값보다 작기 때문에 탐색하려는 배열의 마지막을 중앙값의 이전 값으로 변경
            else
                first = mid + 1; // 왜 +1을 하였을까? -> 타겟이 중앙값보다 크기 때문에 탐색하려는 배열의 처음을 중앙값 오른쪽으로 다시 설정
        }
    }
    return -1; // 찾지 못했을 때 반환되는 값
}

int main(void)
{
    int arr[] = {1, 3, 5, 7, 9};
    int idx;

    idx = BSearch(arr, sizeof(arr) / sizeof(int), 7);
    if (idx == -1)
        printf("탐색 실패\n");
    else
        printf("타겟 저장 인덱스: %d \n", idx);

    idx = BSearch(arr, sizeof(arr) / sizeof(int), 4);
    if (idx == -1)
        printf("탐색 실패\n");
    else
        printf("타겟 저장 인덱스: %d \n", idx);

    return 0;
}