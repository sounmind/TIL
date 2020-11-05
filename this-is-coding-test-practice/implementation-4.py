string = input()

answer = []
sum = 0

for i in string:
    if i.isalpha():
        answer.append(i)
    else:
        sum += int(i)

answer.sort()

if sum != 0:
    answer.append(str(sum))

print("".join(answer))
