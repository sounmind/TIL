n, k = map(int, input().split(" "))
result = 0
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k  # target = k로 나누어 떨어지는 n과 같거나 작은 수 중 최댓값
    result += n - target  # result는 1로 빼야 할 수
    n = target
    # N이 K보다 작을 때  (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k
# 마지막으로 result에 남은 N을 1씩 뺀 횟수 더하기
result += n - 1
print(result)
