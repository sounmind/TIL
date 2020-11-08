# 알고리즘 콘테스트 ([고리콘](https://www.acmicpc.net/contest/view/558))

[2020 경북대학교 Goricon Open Contest](https://www.acmicpc.net/contest/view/558)

1. 사토르 마방진

    ```python
    def init():
        n = int(input())
        rows = list(input() for _ in range(n))

        for i, row_1 in enumerate(rows):
            str_cmp = ""
            for row_2 in rows:
                str_cmp += row_2[i]
            if row_1 != str_cmp:
                print("NO")
                return
        print("YES")
        return

    init()
    ```

2. 긴급 회의

    ```python
    def init():
        n = int(input())
        votes = input().split(" ")
        # 투표 현황
        vote_status = [0 for i in range(n+1)]

        for vote in votes:
            vote_status[int(vote)] += 1

        # 퇴출자 정하기
        # 1. 가장 표를 많이 받은 사람 ( 두 명 이상일 경우 퇴출 X)
        max_vote = max(vote_status)
        # 가장 표를 많이 받은 사람의 색인
        max_player = vote_status.index(max_vote)
        # 가장 표를 많이 받은 사람이 없고 건너뛴 게 가장 많다면
        if max_player == 0:
            vote_status[0] = 0  # 무효표는 초기화
            max_vote = max(vote_status)
            max_player = vote_status.index(max_vote)  # 그 다음 표를 많이 받은 사람

        # 가장 표를 많이 받은 사람이 두 명 이상일 경우
        if vote_status.count(max_vote) > 1:
            print("skipped")
            return
        else:
            print(max_player)

    init()
    ```

3. 미아 노트

    ```python
    # 미아 노트 복원
    def init():
        N, H, W = map(int, input().split(" "))
        rows = list(input() for _ in range(H))
        answer = ""
        # H*W 크기의 박스안에 있는 값은 모두 같은 값이 번진것이다.
        # 즉, 그 박스 안의 하나만 알고 그 값을 알 수 있고, 모두 물음표일 때만 모른다.
        for i in range(0, N * W, W):
            box = ""
            for row in rows:
                box += row[i : i + W]
            for ch in box:
                if ch != "?":
                    answer += ch
                    break
            if len(box) == box.count("?"):
                answer += "?"
            box = ""

        print(answer)

    init()
    ```

4. 에너지 드링크

    ```python
    # 가장 양이 많은 음료에 가장 양이 적은 음료의 절반을 계속 더하자
    def init():
        n = int(input())
        drink_list = list(map(int, input().split(" ")))
        drink_list.sort()
        # print(drink_list)
        max_drink = drink_list[-1]
        sum_drink = max_drink
        drink_list = drink_list[:-1]
        for i in range(n - 1):
            min_drink = drink_list[i]
            sum_drink += min_drink / 2

        print(sum_drink)
        return

    init()
    ```