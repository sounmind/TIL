#include <stdio.h>

int BSearchRecur(int ar[], int first, int last, int target)
{
    int mid;
    if (first > last) // -1�� ��ȯ�� Ž���� ���и� �ǹ�
        return -1;    // Ž�� ����� �߾��� ã�´�
    mid = (first + last) / 2;

    if (ar[mid] == target)
        return mid; // Ž���� Ÿ���� �ε��� �� ��ȯ
    else if (target < ar[mid])
        return BSearchRecur(ar, first, mid - 1, target);
    else
        return BSearchRecur(ar, mid + 1, last, target);
}

int main(void)
{
    int arr[] = {1, 3, 5, 7, 9};
    int idx;

    idx = BSearchRecur(arr, 0, sizeof(arr) / sizeof(int) - 1, 7);
    if (idx == -1)
        printf("Ž�� ���� \n");
    else
        printf("Ÿ�� ���� �ε���: %d \n", idx);

    idx = BSearchRecur(arr, 0, sizeof(arr) / sizeof(int) - 1, 4);
    if (idx == -1)
        printf("Ž�� ���� \n");
    else
        printf("Ÿ�� ���� �ε���: %d \n", idx);

    return 0;
}