import time

row = "0abcdefgh"
loc = input()
start_time = time.time()
chances = []
x = int(row.index(loc[0]))  # 방법1: 리스트 인덱스 활용하여 얻기
x = int(ord(loc[0])) - int(ord("a")) + 1  # 방법2: 아스키코드로 int형 좌표 얻기
y = int(loc[1])


# 하나의 위치에 따라 8개의 이동 가능한 위치가 있다.
chances = [
    [x - 2, y - 1],
    [x - 2, y + 1],
    [x - 1, y + 2],
    [x - 1, y - 2],
    [x + 1, y - 2],
    [x + 1, y + 2],
    [x + 2, y - 1],
    [x + 2, y + 1],
]

# 해당 위치가 체스판을 벗어나는지 확인하고 가능한 경우를 계산한다
count = 8
for chance in chances:
    if chance[0] < 1 or chance[1] < 1:
        count -= 1

print(count)
end_time = time.time()  # 측정 종료
print("time: ", end_time - start_time)  # 수행 시간 출력