import time

loc = input()
start_time = time.time()
chances = []
x = int(ord(loc[0])) - int(ord("a")) + 1  # 방법2: 아스키코드로 int형 좌표 얻기
y = int(loc[1])


# 하나의 위치에 따라 8개의 이동 가능한 위치가 있다.
chances = [
    [-2, -1],
    [-2, +1],
    [-1, +2],
    [+1, -2],
    [-1, -2],
    [+1, +2],
    [+2, -1],
    [+2, +1],
]

# 해당 위치가 체스판을 벗어나는지 확인하고 가능한 경우를 계산한다
count = 8
for chance in chances:
    next_x = x + chance[0]
    next_y = y + chance[1]
    if (8 < next_x or next_x < 1) or (8 < next_y or next_y < 1):
        count -= 1

print(count)
end_time = time.time()  # 측정 종료
print("time: ", end_time - start_time)  # 수행 시간 출력