import time

# # 나의 풀이
# numbers = input()
# start_time = time.time()
# number_list = [int(i) for i in numbers]

# result = 0
# # 0이 나오면 무조건 더하기
# # 1이 나오면 무조건 더하기
# # 결과가 0이면 다음 숫자는 무조건 더하기
# # 첫번째 숫자면 무조건 더하기
# for i, number in enumerate(number_list):
#     if i == 0 or number == 0 or number == 1 or result == 0 or result == 1:
#         result += number
#     else:
#         result *= number
# print(result)  # "123456789" -> 0.0010020732879638672

# end_time = time.time()  # 측정 종료
# print("time: ", end_time - start_time)  # 수행 시간 출력

# 교재 소스 코드
data = input()
start_time = time.time()
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)  # "123456789" 0.0009980201721191406
end_time = time.time()  # 측정 종료
print("time: ", end_time - start_time)  # 수행 시간 출력