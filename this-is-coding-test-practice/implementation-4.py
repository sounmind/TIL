string = input()
answer = ""
sum = 0
array = sorted(list(string))

for i in array:
    try:
        sum += int(i)
    except:
        answer += i

print(answer + str(sum))
