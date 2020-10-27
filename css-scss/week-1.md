# **TIL**

---

## **노마드코더 | [CSS Layout 2주 완성반](https://nomadcoders.co/css-layout-masterclass/)**

- 문제
    - display 속성
        - inline-box
        - block

        element 간격을 일일이 지정해야 하고, 그 간격이 반응해서 바뀌지 못하는 문제점이 있다.

    - 이 문제를 어떻게 해결할 수 있을까? → Flexbox를 사용하자!

# #1 Flexbox

---

- flexbox의 요소들을 옮기고 싶다면 요소 바깥에 flexbox-container를 만들면 된다.
    - css에서 disaply:flex 속성을 부여하는 element가 flexbox-container가 된다.
    - flexbox가 되는 요소들은 flexbox-container의 직계 자손들이다.
- flex-direction
    - flex-direction: row (기본 방향, 적지 않아도 기본으로 적용된다, default, main axis == horizontal axis)
        - main axis가 horizontal 일 때, cross axis 는 vertical 이다.
    - flex-direction: column (적어줘야지 적용된다)
        - main axis와 cross axis가 반대가 된다.
- justify-content
    - 수평축(Main Axis)에 있는 flex children의 위치를 변경한다.
    - justfiy-content: center
    - justfiy-content: space-around
- align-items
    - cross axis 방향으로 item을 옮긴다.
    - align-items: stretch → flex father의 높이까지 요소가 위 아래로 뻗는다.
    - align-items: center → flex father의 높이의 중앙에 요소가 배치된다.
    - align-items: end → flex father의 높이의 가장 아래에 요소가 배치된다.
- align-self
    - 기본적으로  align-items와 같지만, 개별 element에도 적용된다.
    - cross axis 방향으로 element 개별적으로 위치를 변화시킨다.
    - align-self: center 세로로 중앙
    - align-self: flex-end 세로로 가장 아래
- order

    > HTML을 바꿀 수 없을 때 유용

    - order의 default 값은 0이다.
    - order 값이 클 수록 뒷 순서에 배치된다.

> flexbox는 width를 신경 쓰지 않고(미리 지정해도 변경되어버림) 오직 같은 줄에 있도록 하는 데 집중한다.

- flex-wrap
    - (기본값) flex-wrap: nowrap

        > 무슨 일이 일어나도 나 아래의 element 들은 같은 줄에 있어야 해! 라는 뜻

    - flex-wrap: wrap

        > 나(container, father) 아래의 요소(element, child)들의 크기를 유지해. 다음 줄로 넘어가도 말이야.

- reverse
    - flex-wrap: wrap-reverse → 아래에서부터 반대로 요소가 배치된다.
    - flex-direction: row-reverse → 행에 있던 요소들의 순서가 반대로 된다.
    - flex-direction: column-reverse → 열에 있던 요소들의 순서가 반대로 된다.
- align-content
    - align-content: flex-start → 행 간 간격이 없어진다.
    - align-content: content → 요소들이 중앙에 배치된다.
    - align-content: space-between → 한 줄은 가장 위에, 한 줄은 가장 아래에 배치
- flex-shrink
    - 기본 값은 1
    - flex-shrink: 2 → 다른 요소보다 2배로 너비가 줄어든다.
- flex-grow
    - 기본 값은 0
    - flex-grow: 1 → 다른 요소보다 2배로 너비가 늘어진다.
    - 남아 있는 공간을 해당 수치만큼 채우게 된다.
- flex-basis
    - child에 적용됨.
    - (flex-direction: column일때) width와 비슷하다. 좀 더 엄밀하게 말하자면, 요소가 변형되기 전 초기 값을 뜻한다.
    - main-axis에서 일어난다.

# 20-10-27 | [Code Challenge](https://repl.it/@sounmind/CSSLAYOUTDAY02#index.html)

---

- 후기
    - 처음에는 flexbox 사용이 낯설어서 당황하다가, 배웠던 것 그대로 써먹으니까 잘 됐다.