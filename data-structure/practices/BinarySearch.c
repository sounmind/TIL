#include <stdio.h>

int BSearch(int array[], int len, int target)
{
    int first = 0;      // Ž�� ����� ���� �ε��� ��
    int last = len - 1; // Ž�� ����� ������ �ε��� ��
    int mid;

    while (first <= last) // �迭�� ó���� ������ ���� �۰ų� ���� ��
    {
        mid = (first + last) / 2; // Ž�� ����� �߾��� ã�´�
        if (target == array[mid]) // �߾ӿ� ����� ���� Ÿ���̶��
        {
            return mid; // Ž�� �Ϸ�!
        }
        else // Ÿ���� �ƴ϶�� Ž�� ����� ������ ���̱�
        {
            if (target < array[mid])
                last = mid - 1; // �� -1�� �Ͽ�����? -> Ÿ���� �߾Ӱ����� �۱� ������ Ž���Ϸ��� �迭�� �������� �߾Ӱ��� ���� ������ ����
            else
                first = mid + 1; // �� +1�� �Ͽ�����? -> Ÿ���� �߾Ӱ����� ũ�� ������ Ž���Ϸ��� �迭�� ó���� �߾Ӱ� ���������� �ٽ� ����
        }
    }
    return -1; // ã�� ������ �� ��ȯ�Ǵ� ��
}

int main(void)
{
    int arr[] = {1, 3, 5, 7, 9};
    int idx;

    idx = BSearch(arr, sizeof(arr) / sizeof(int), 7);
    if (idx == -1)
        printf("Ž�� ����\n");
    else
        printf("Ÿ�� ���� �ε���: %d \n", idx);

    idx = BSearch(arr, sizeof(arr) / sizeof(int), 4);
    if (idx == -1)
        printf("Ž�� ����\n");
    else
        printf("Ÿ�� ���� �ε���: %d \n", idx);

    return 0;
}