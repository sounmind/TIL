# TIL

---

## [노마드코더 | 바닐라JS 2주 완성반](https://nomadcoders.co/c/vanillajs-challenge/lobby)

---

[2주 과정 진도표](https://nomadcoders.co/faq/schedule-vanillajs) | 2020-10-05 ~ 2020-10-18

# 20-10-12 | Code Challenge | Events, localStorage

---

### 과제 목표

---

- To Do 리스트 만들기
    1. 입력
    2. 브라우저의 지역 저장소에 내용이 저장되어야 함. → 새로고침했을 때 데이터를 그대로 불러올 수 있어야 함.
    3. 리스트를 Pending, Finished 두 하위 리스트로 나눠, 버튼을 눌렀을 때 자유롭게 리스트 간 이동과 삭제를 할 수 있어야 함.

### 소감

---

- 너무 힘들었다.
- filter()에서 오류가 있었는데, parseInt()로 모두 숫자로 변형시켜줬다.
- 시간을 소비하는 과정에서, 그래도 to do list 의 흐름을 체내화 시킨 것 같아서 좋은 점은 있었다.

### 필요개념

---

- JSON.stringify()
- Math
    - Math.floor()
    - Math.random()
- list
    - push
    - filter()
    - forEach()
- event
    - target
- DOM
    - parentNode
    - createElement()
    - appendChild()
    - innerHTML
    - innerText
    - removeChild()
- parseInt(string, radix)

# 20-10-14 | Code Challenge | JS Casino

---

- 과제 내용
    - 플레이 버튼을 누를 때마다 랜덤 넘버 생성하여 사용자가 입력한 숫자와 일치할 경우 이기고 일치하지 않을 경우 지는 화면을 출력하는 게임 만들기
- 감상
    - 이전 과제보다 훨씬 쉬웠다.


# 20-10-16 | Code Challenge | JS Calculator

---

- 계산기 만들기
    - 사칙연산, 초기화, '=' 버튼, '=' 버튼 누르지 않고도 계속되는 연산의 결과가 입력창에 표시되어야 함.
- 후기 → [소스 코드 링크](https://codesandbox.io/s/2020-10-17-vanillajs-calculator-qo7of?file=/src/index.js)
    - 계산기가 연산자를 누르고 우측에 숫자를 누른 즉시 계산이 되는 게 아니라, 이전 연산자를 기억하고 있어야 해서 애로사항이 많았다. 헷갈리고 복잡했다.
    - 아, 더 멋지게 만들 수 있을 것 같은데 시간이 없어서 일단 이렇게만 해놓고 다시 만들러 와야겠다.
        - 리팩토링이 필요하다!