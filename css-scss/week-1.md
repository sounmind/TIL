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