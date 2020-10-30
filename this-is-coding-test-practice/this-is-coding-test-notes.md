[(이코테 2021 강의 몰아보기) 1. 코딩 테스트 출제 경향 분석 및 파이썬 문법 부수기](https://www.youtube.com/watch?v=m-9pAwq1o3w&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

- 코딩 테스트 출제 경향 분석 및 파이썬 문법 부수기

    # 코딩테스트 개요 및 출제경향

    # 알고리즘 성능 평가

    ## 복잡도

    - 복잡도의 종류
        - 시간 복잡도
        - 공간 복잡도
    - 복잡도의 표기법
        - 빅오 표기법
            - 가장 빠르게 증가하는 항만을 고려하는 표기법. 함수의 상한만을 나타내게 된다.
    - 시간 복잡도 계산해보기
        - 모든 이중 반복문의 시간복잡도가 O(N^2)인 것은 아니다. 소스코드가 내부적으로 다른 함수를 호출한다면, 그 함수의 시간 복잡도까지 고려해야 한다.

    ## 알고리즘 설계 Tip

    - 일반적으로 CPU 기반의 개인 컴퓨터나 채점용 컴퓨터에서 연산 횟수가 5억을 넘어가는 경우:
        - C언어 기준 통상 1~3초, Python은 5~15초 가량의 시간이 소요된다.
            - PyPy의 경우 때때로 C언어보다도 빠르게 동작하기도 한다. 그러니 시간이 초과됐을 경우 PyPy로도 제출해보는 것도 좋을 수 있다.
    - 코딩 테스트 문제에서 시간제한은 통상 1~5초 가량이라는 점에 유의. 혹여 문제에 명시되어 있지 않은 경우 대략 5초라고 생각하고 문제를 푸는 것이 합리적.

    ### 요구사항에 따라 적절한 알고리즘 설계하기

    - 문제에서 가장 먼저 확인해야 하는 내용은 시간제한(수행시간 요구사항)이다.
    - 시간제한이 1초인 문제에서 일반적인 기준은 다음과 같다.
        1. N의 범위가 500인 경우: 시간복잡도가 O(N^3)인 알고리즘 설계 시 문제를 풀 수 있다.
        2. N의 범위가 2000인 경우: 시간복잡도가 O(N^2)인 알고리즘 설계 시 문제를 풀 수 있다.
        3. N의 범위가 100000인 경우: 시간복잡도가 O(NlogN)인 알고리즘 설계 시 문제를 풀 수 있다.
        4. N의 범위가 10000000인 경우: 시간복잡도가 O(N)인 알고리즘 설계 시 문제를 풀 수 있다.

    ## 일반적인 알고리즘 문제 해결 과정

    > 나는 이 문제를 간결하고 창의적으로 풀 수 있다고 스스로 확신을 갖고 문제 풀이를 시작하기

    1. 지문 읽기 및 컴퓨터적 사고
    2. 요구사항(복잡도) 분석
    3. 문제 해결을 위한 아이디어 찾기
    4. 소스코드 설계 및 코딩

    > 일반적으로 대부분의 문제 출제자들은 핵심 아이디어를 알아낸다면 간결하게 소스코드를 작성할 수 있는 형태로 문제를 출제한다.

    ## 수행 시간 측정 소스코드 예제

    ```python
    import time
    start_time = time.time()  # 측정 시작
    # ...
    # 소스 코드
    # ...
    end_time = time.time() # 측정 종료
    print("time: ", end_time - start_time) # 수행 시간 출력
    ```

    # 파이썬 문법

    ## 파이썬 | 자료형

    ### 정수형

    ### 실수형

    - 소수부가 0일 때 0을 생략하거나 정수부가 0일때 0을 생략할 수 있다.
    - 지수표현방식 (기본적으로 실수형)
        - 파이썬에서는 e나 E를 이용한 지수표현방식을 이용할 수 있다.
        - e나 E 다음에 오는 수는 10의 지수부를 의미한다. (`1e9` → 10의 9제곱)
        - 지수 표현 방식은 임의의 큰 수를 표현하기 위해 자주 사용된다.
        - **최단 경로 알고리즘에서는 도달할 수 없는 노드에 대하여 최단 거리를 무한(`INF`)로 설정하곤 한다.**
        - 이때 가능한 최댓값이 10억 미만이라면 무한(`INF`)의 값으로 `1e9`를 이용할 수 있다.
    - 오늘날 가장 널리 쓰이는 IEEE754 표준에서는 실수형을 저장하기 위해 4바이트, 또는 8바이트의 고정된 크기의 메모리를 할당하므로, 컴퓨터 시스템은 실수 정보를 표현하는 정확도에 한계를 가진다.
        - 예를 들어 10진수 체계에서 0.3 + 0.6 = 0.9로 정확히 떨어진다. 하지만 2진수에서는 0.9를 정확히 표현할 수 있는 방법이 없다. 컴퓨터는 최대한 0.9와 가깝게 표현하지만, 미세한 오차가 발생하게 된다.
        - 권장되는 해결 방법 → `round()` 반올림
    - 수 자료형의 연산
        - 수 자료형에서 사칙연산과 나머지 연산자가 많이 사용된다.
        - 하지만 나누기 연산자(/)는 주의해서 사용해야 한다.
            - 파이썬에서 나누기 연산자(/)는 나눠진 결과를 실수형으로 반환한다.
        - 다양한 로직을 설계할 때 나머지 연산자(%)를 이용해야 할 때가 많다.
        - 파이썬에서는 몫을 얻기 위해 몫 연산자(//)를 사용한다.
        - 이외에도 거듭 제곱 연산자(**)를 비롯해 다양한 연산자들이 존재한다.

    ### 리스트 자료형

    - 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
        - 사용자 입장에서 C나 Java에서의 배열(Array)의 기능 및 연결 리스트와 유사한 기능을 지원한다.
        - 리스트 대신에 배열 혹은 테이블이라고 부르기도 한다.
        - 모든 값이 0인 1차원 리스트 초기화

            ```python
            n=10
            a=[0]*n # [0,0,0,0,0,0,0,0,0,0]
            ```

    - 리스트의 인덱싱과 슬라이싱
        - 리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때는 슬라이싱을 이용한다.
            - 대괄호 안에 콜론(:)을 넣어서 시작 인덱스와 끝 인덱스를 설정할 수 있다.
            - 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정한다.
    - 리스트 컴프리헨션
        - 리스트를 초기화하는 방법 중 하나.
            - 대괄호 안에 **조건문**과 **반복문**을 적용하여 리스트를 초기화할 수 있다.

                ```python
                array = [i for i in range(5)] # [0, 1, 2, 3, 4]
                array = [i for i in range(10) if i % 2 == 1] # [1, 3, 5, 7, 9]
                array = [i * i for i in range(1, 10)] # 1부터 9까지 수들의 제곱 값을 포함하는 리스트
                ```

        - 리스트 컴프리헨션은 2차원 리스트를 초기화할 때 효과적으로 사용될 수 있다.
        - 특히 N * M 크기의 2차원 리스트를 한 번에 초기화 할 때 유용하다.
            - **좋은 예시: array = [[0] * m for _ in range(n)]**
        - 만약 2차원 리스트를 초기화할 때 다음과 같이 작성하면 예기치 않은 결과가 나올 수 있다.
            - 잘못된 예시: array = [[0] * m] * n

                위 코드는 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식된다.

                ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9c034a3f-cdcd-4dbb-bf22-4a7c33c199dc/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9c034a3f-cdcd-4dbb-bf22-4a7c33c199dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201030T182042Z&X-Amz-Expires=86400&X-Amz-Signature=1095cecaea1a16bfbe6252ad3a00996024120638ac0c312fa39e5dd55d1964bd&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

    - 언더바는 언제 사용하는가?
        - 파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용한다.
    - 리스트 관련 기타 메서드

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7cd7f43e-6021-4582-9874-515c26a21eea/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7cd7f43e-6021-4582-9874-515c26a21eea/Untitled.png)

    - 리스트에서 특정 값을 가지는 원소를 모두 제거하기

        ```python
        a = [1,2,3,4,5,5,5]
        remove_set = {3, 5} # 집합 자료형 (집합 자료형은 추후에 다룸)

        # remove_list에 포함되지 않은 값만을 저장
        result = [i for i in a if i not in remove_set]
        print(result) # [1, 2, 4]
        ```

    ### 문자열 자료형

    - 문자열 변수를 초기화할 때는 큰따옴표나 작은따옴표를 이용한다.
    - 문자열 안에 큰따옴표나 작은따옴표가 포함되어야 하는 경우가 있다.
        - 전체 문자열을 큰(작은)따옴표를 구성하는 경우, 내부적으로 작은(큰)따옴표를 포함할 수 있다.
        - 혹은 백슬래시(\)를 사용하면, 큰따옴표나 작은따옴표를 원하는 만큼 포함시킬 수 있다.
    - 문자열 연산
        - 문자열 변수에 덧셈을 이용하면 문자열이 더해져 연결된다.
        - 문자열 변수를 특정한 양의 정수와 곱하는 경우, 문자열이 그 값만큼 여러 번 더해진다.
        - 문자열도 리스트와 마찬가지로 인덱싱과 슬라이싱을 이용할 수 있다. 하지만 문자열은 특정 인덱스의 값을 변경할 수 없다(Immutable).

    ### 튜플 자료형

    - 튜플 자료형은 리스트와 유사하지만 다음과 같은 문법적 차이가 있다.
        - 튜플은 한 번 선언된 값을 변경할 수 없다.
        - 리스트는 대괄호([])를 이용하지만, 튜플은 소괄호(())를 이용한다.
    - 튜플은 리스트에 비해 상대적으로 공간 효율적이다.
    - 튜플을 사용하면 좋은 경우
        - 서로 다른 성질의 데이터를 묶어서 관리해야 할 때, **최단 경로 알고리즘에서는 (비용, 노드 번호)의 형태**로 튜플 자료형을 자주 사용한다.
        - 데이터의 나열을 **해싱(Hashing)의 키 값**으로 사용해야 할 때, 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있다.
        - 리스트보다 **메모리를 효율적**으로 사용해야 할 때

    ### 사전 자료형

    - 사전 자료형은 키(Key)와 값(Value)의 쌍을 데이터로 가지는 자료형이다. 원하는 '변경 불가능한 자료형'을 키로 사용할 수 있다.
    - 파이썬의 사전 자료형은 해시 테이블(Hash Table)을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.
    - 사전 자료형 관련 메서드
        - 사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 메서드를 지원한다.
            - 키 데이터만 뽑아서 리스트로 이용할 때는 `keys()` 함수를 이용
            - 값 데이터만 뽑아서 리스트로 이용할 때는 `values()` 함수를 이용

    ### 집합 자료형

    - 집합의 특징
        - 중복을 허용하지 않는다.
        - 순서가 없다.
    - 집합은 리스트 혹은 문자열을 이용해서 초기화할 수 있다. 이때 `set()` 함수를 이용한다.
    - 혹은 중괄호({})안에 각 원소를 콤파(,)를 기준으로 구분하여 삽입함으로써 초기화 할 수 있다.
    - 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.
    - 집합 자료형의 연산
        - 기본적인 집합 연산으로 합집합(`a ㅣ b`), 교집합(`a & b`), 차집합(`a - b`) 연산이 있다.
    - 집합 자료형 관련 함수
        - `add()`, `update()`, `remove()`
    - 사전 자료형과 집합 자료형의 특징
        - 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있다.
        - 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 없을 수 없다. 사전의 키 혹은 집합의 원소를 이용해 O(1)의 시간복잡도로 조회한다.
        - 

    ## 파이썬 | 기본 입출력

    ### 자주 사용되는 표준 입력 방법

    - input() 함수는 한 줄의 문자열을 입력 받음.
    - map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용.
        - 예시1) 공백을 기준으로 구분된 데이터를 입력 받을 때는 다음과 같이 사용한다.
            - `list(map(int, input().split()))`
                - `input().split()` → 입력된 문자열이 공백으로 구분된 리스트가 된다.
        - 예시2) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용한다.
            - `a, b, c = map(int, input().split())`

    ### 빠르게 입력 받기

    - 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우가 있다.
        - 파이썬의 경우 sys 라이브러리에 정의되어 있는 `sys.stdin.readline()` 메서드를 이용한다. 단, 입력 후 엔터(Enter)가 줄바꿈 기호로 입력되므로 `rstrip()` 메서드를 함께 사용한다.

            ```python
            import sys
            # 문자열 빠르게 입력 받기
            data = sys.stdin.readline().rstrip()
            ```

    ### 자주 사용되는 표준 출력 방법

    - 파이썬에서 기본 출력은 print() 함수를 이용한다. 각 변수를 콤마(,)를 이용하여 띄어쓰기로 구분하여 출력할 수 있다.
    - print()는 기본적으로 출력 이후에 줄 바꿈을 수행한다. 줄 바꿈을 원치 않는 경우 'end' 속성을 이용할 수 있다.
    - f-string 예제
        - 파이썬 3.6부터 사용 가능하며, 문자열 앞에 접두사 'f'를 붙여 사용한다.
        - 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있다.

    ## 파이썬 | 조건문

    ---

    - 조건문은 프로그램의 흐름을 제어하는 문법. 조건문을 이용해 조건에 따라서 프로그램의 로직을 설정할 수 있다.

    ### 파이썬의 기타 연산자

    - 다수의 데이터를 담는 자료형을 위해 `in` 연산자와 `not in` 연산자가 제공된다. **리스트, 튜플, 문자열, 딕셔너리** 모두에서 사용이 가능하다.

    ### 조건문의 간소화

    - 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있다.

        ```python
        score = 85
        if score >= 80: result = "Success"
        else: result = "Fail"
        ```

    - 조건부 표현식(Conditional Expression)은 if ~ else 문을 한 줄에 작성할 수 있도록 해준다.

        ```python
        score = 85
        result = "Success" if score >= 80 else "Fail"
        ```

    ### 파이썬 조건문 내에서의 부등식

    - 다른 프로그래밍 언어와 다르게 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있다.

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1bb7ecac-44e7-403b-b8c9-d5247aedf036/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1bb7ecac-44e7-403b-b8c9-d5247aedf036/Untitled.png)

    ## 반복문

    ---

    - 특정한 소스코드를 반복적으로 실행하고자 할 때 사용하는 문법입니다.
    - 파이썬에서는 while문과 for문이 있는데, 어떤 것을 사용해도 상관 없습니다.
        - 다만 코딩 테스트에서의 실제 사용 예시를 확인해 보면, for문이 더 간결한 경우가 많습니다.

    ### 반복문: for문

    - for문에서 연속적인 값을 차례대로 순회할 때는 `range()`를 주로 사용한다. 이때 `range(시작 값, 끝 값+1)` 형태로 사용한다. 인자를 하나만 넣으면 자동으로 시작 값은 0이 된다.

    ### 파이썬의 continue 키워드

    - 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 continue를 사용한다.

    ### 파이썬의 break 키워드

    - 반복문을 즉시 탈출하고자 할 때 break를 사용한다.

    ## 파이썬 | 함수와 람다 표현식

    ---

    ### 함수

    - 함수란 특정한 작업을 하나의 단위로 묶어 놓은 것을 의미한다. 함수를 사용하면 불필요한 소스코드의 반복을 줄일 수 있다.
    - 함수의 종류
        - 내장 함수
        - 사용자 정의 함수
    - 함수 정의하기
        - 매개변수(parament): 함수 내부에서 사용할 변수
            - 파라미터의 변수를 직접 지정할 수 있다. 이 경우 매개변수의 순서가 달라도 상관이 없다.
        - 반환 값: 함수에서 처리 된 결과를 반환
        - 인자(argument): 코드에서 함수의 매개변수 자리에 넣는 값
        - global 키워드
            - global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 됩니다.
        - 여러 개의 반환 값
            - 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있다.
            - 팩킹(여러 개를 반환 값으로 전달하는 것)과 언팩킹(여러 개의 반환 값을 변수에 대입하는 것)

    ### 람다 표현식

    - 람다 표현식을 이용하면 함수를 간단하게 작성할 수 있다. 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징이다.

    ```python
    def add(a, b):
    	return a + b
    # 일반적인 add() 메서드 사용
    print(add(3, 7))

    # 람다 표현식으로 구현한 add() 메서드
    print((lambda a, b: a + b)(3, 7))
    ```

    - 람다 표현식 예시: 내장 함수에서 자주 사용되는 람다 함수

        > 매개변수에 어떻게 대입이 되는 것인지 잘 모르겠다...

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7eac3ca7-afe9-4931-90ab-645ea5752032/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7eac3ca7-afe9-4931-90ab-645ea5752032/Untitled.png)

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a30cca62-5ed4-4e88-b427-b68bb6b8b787/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a30cca62-5ed4-4e88-b427-b68bb6b8b787/Untitled.png)

    ## 실전에서 유용한 표준 라이브러리

    ---

    - 내장 함수: 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공한다. 파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포함하고 있다.
        - 예

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dd0a884a-04a5-44b3-b307-200020b1412a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dd0a884a-04a5-44b3-b307-200020b1412a/Untitled.png)

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cdd93d55-27e0-418b-b69c-fdb3b52cd4d6/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cdd93d55-27e0-418b-b69c-fdb3b52cd4d6/Untitled.png)

    - itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공한다. 특히 **순열과 조합** 라이브러리는 코딩 테스트에서 자주 사용된다. **중복순열과 중복조합**도 있다!
        - 예

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/228ec4d5-759e-48d8-941d-fcb54a5d66f2/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/228ec4d5-759e-48d8-941d-fcb54a5d66f2/Untitled.png)

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3ec67e5c-60b0-4b84-8049-17086aace8aa/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3ec67e5c-60b0-4b84-8049-17086aace8aa/Untitled.png)

    - heapq: 힙(Heap) 자료구조를 제공한다. 일반적으로 우선순위 큐 기능을 구현하기 위해 사용된다.
    - bisect: 이진 탐색(Binary Search) 기능을 제공한다.
    - collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함한다.
        - 예

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f18effb0-c739-4201-bfdf-64996ab6f7e1/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f18effb0-c739-4201-bfdf-64996ab6f7e1/Untitled.png)

    - math: 필수적인 수학적 기능을 제공한다. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함한다.
        - 예

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d89b3b0c-1fae-47cd-b168-b04b4d31b8d5/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d89b3b0c-1fae-47cd-b168-b04b4d31b8d5/Untitled.png)

- 그리디 & 구현

    # 그리디 알고리즘

    - 그리디 알고리즘(탐욕법)은 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미한다.
    - 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구한다.
    - 그리디 해법은 그 정당성 분석이 중요하다
        - 단순히 가장 좋아보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는 검토해야 한다.
    - 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많다.
    - 대부분의 코딩테스트 그리디 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있어야 풀리도록 출제된다.
    - 문제1 | 거스름 돈
        - 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다. 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 동전의 최소 개수를 구하시오. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
        - 정당성 분석
            - 가장 큰 화폐 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유는?
                - **가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문이다.**

                그리디 알고리즘 문제에서는 이처럼 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 한다.

        - 시간복잡도 분석
            - 화폐의 종류만큼 반복이 수행되므로 시간 복잡도는 O(N)이다.
    - 문제2 | 1이 될 때까지

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2f924181-9efa-4f2f-99fa-411ca54704ad/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2f924181-9efa-4f2f-99fa-411ca54704ad/Untitled.png)

    - 문제3 | 곱하기 혹은 더하기

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/55cd31b3-f6d5-426d-84b3-4920d61cb4f3/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/55cd31b3-f6d5-426d-84b3-4920d61cb4f3/Untitled.png)

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f25f931-52ae-43a0-9a33-859578d5e13b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f25f931-52ae-43a0-9a33-859578d5e13b/Untitled.png)

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/24641566-2f39-4c67-ad2b-b3bc71d9ccfc/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/24641566-2f39-4c67-ad2b-b3bc71d9ccfc/Untitled.png)

    - 문제4 | 모험가 길드

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ee06f8c0-4b68-4ff0-ba56-7304f1728e92/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ee06f8c0-4b68-4ff0-ba56-7304f1728e92/Untitled.png)

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d836a938-34ea-4575-a94e-6eb72e15c1e5/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d836a938-34ea-4575-a94e-6eb72e15c1e5/Untitled.png)

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df9b6a76-1c22-4d1d-a872-b8b62eecb84b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df9b6a76-1c22-4d1d-a872-b8b62eecb84b/Untitled.png)

        나머지는 마을에 그대로 남아 있어도 된다! 그래서 나머지는 신경 안 써도 된다!

    # 구현

    - 구현이란, 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정이다.
    - 흔히 알고리즘 대회에서 구현 유형의 문제란 무엇을 의미할까?
        - 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 지칭한다.
        - 예시
            1. 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
            2. 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
            3. 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
            4. 적절한 라이브러리를 찾아서 사용해야 하는 문제
    - 일반적으로 알고리즘 문제에서의 2차원 공간은 **행렬**(Matrix)의 의미로 사용된다.
    - 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 **방향 벡터**가 자주 활용된다.

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/76f75c95-b476-4c46-b4d9-f9b0a736dc56/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/76f75c95-b476-4c46-b4d9-f9b0a736dc56/Untitled.png)

    - 문제1 상하좌우

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4714f8aa-4651-4582-b164-7d783f5cb516/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4714f8aa-4651-4582-b164-7d783f5cb516/Untitled.png)

        - 문제의 아이디어는
            - 열
                - 왼쪽
                - 오른쪽
            - 행
                - 위로
                - 아래로

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c0d53bad-aed0-41ea-a9a1-4cf42e925f05/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c0d53bad-aed0-41ea-a9a1-4cf42e925f05/Untitled.png)

    ## 구현 문제 풀이

    - 문제2 시각

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/36e8c3a5-51f8-4d79-bda6-ca4c71d825bd/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/36e8c3a5-51f8-4d79-bda6-ca4c71d825bd/Untitled.png)

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df357cd2-47c8-4a08-b168-9d5580557a76/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df357cd2-47c8-4a08-b168-9d5580557a76/Untitled.png)