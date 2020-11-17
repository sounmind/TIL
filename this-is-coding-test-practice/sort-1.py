N, K = map(int, input().split(" "))
A = list(map(int, input().split(" "))).sort()
B = list(map(int, input().split(" "))).sort(reverse=True)

for i in range(K):  # K번의 교체
    # A의 원소가 최대가 되도록,
    # A의 원소가 B의 원소보다 작은 경우
    if A[i] < B[i]:
        # 두 원소를 교체
        A[i], B[i] = B[i], A[i]
    else:  # A의 원소가 B의 원소보다 크거나 같을 때 반복문 탈출
        break

print(sum(A))