학습 동기: 코멘토 직무부트캠프에서 Django로 웹사이트 개발을 하고 있는데, 내가 만들려고 하는 웹사이트 데이터 흐름을 더욱 잘 이해하고 다룰 수 있기 위해 관계형 데이터베이스 공부가 필요하다고 생각했다.

# 생활코딩 | [관계형 데이터베이스의 필요성](https://opentutorials.org/course/3161/19544)

---

기본적으로 노션으로 정리했다 → [링크](https://www.notion.so/DATABASEn-3d55ac20d63549f3a037a6bb9da9d307)

# 생활코딩 | 관계형 데이터베이스 모델링

---

[생활코딩](https://opentutorials.org/course/3883) | [유튜브 재생목록](https://www.youtube.com/playlist?list=PLuHgQVnccGMDF6rHsY9qMuJMd295Yk4sa)

## 관계형 데이터베이스 모델링 | 전체흐름

---

내가 현재 만들고 싶은 (예: 현재 진행하고 있는 직무부트캠프에서 만들려고 하는 웹사이트) 것을 기준으로 작성해보자.

### 1. 업무파악

> '말(verbal thing)'의 기능을 불신하자. → 생각을 더 정확히 알도록 하자.

- 나 또는 의뢰자가 하고자 하는 일을 파악하는 것
- 기획 → [ovenapp](https://ovenapp.io/) 으로 프로토타입 만들기
  - 이해 당사자들이 모여 작성하는 것이 좋다.

### 2. 개념적 데이터 모델링

- 필터
- 그림으로 그리기
- ERD (Entity Releationship Diagram)

  > ERD는 현실을 3개의 관점으로 바라볼 수 있는 파인더를 우리에게 제공해준다.

  1. **정보**를 발견하고
  2. 서로 **연관**된 정보를 **그룹**핑하여 인식하고
  3. 정보 **그룹** 사이의 **관계**를 인식하고

  그것을 다른 사람에게 표현할 수 있게 해준다.

  ### ERD의 구성요소

  ***

  - Entity(table) 와 Attribute(column)
    - Entity → 저자, 글, 댓글
    - Attribute → (글의)제목, 본문, 생성일 | (저자의)이름, 소개, 생성일 | (댓글의)제목, 본문, 저자, 생성일
  - Realation (PK, FK)
    - Relationship with Entities
  - Tuple(행: Row, 튜플)

- ERD 그리기 → 툴 [draw.io](https://app.diagrams.net/)

  - Entity와 Attribute 정의하기
  - Identifier(식별자) 정의하기
    - 후보키(candidate key) → 식별자가 될 수 있는 키
      - 기본키(primary key), 인조키
      - 대체키(alternate key)
      - 중복키(composite key) → 다대다 관계일 경우
    - 왜래키 → 외부에 있는 테이블의 데이터를 구분할 수 있는 키
  - Realation 설정하기 → 다이아몬드 모양으로 작성하기
    - [Cardinality](https://ko.dict.naver.com/#/entry/koko/600cef16808e4d1a87fd2ed4636c87ce) | 기수
      - 1 대 1 관계
      - 1 대 N 관계
      - N 대 M 관계, 다대다 관계
        - 현실에서는 구현할 수 없기 때문에 중간에 연결 테이블을 만든다.
        - 근데 Django에서는 따로 필드가 있는데, 어떻게 구현된 것일까?
    - Optionality | 선택 사항
      - 저자는 댓글을 작성하지 않을 수도 있다. → 저자에게 댓글은 옵션이다. 관계선에서 댓글 쪽에 동그라미 표시가 있음.
      - 각 댓글은 반드시 저자가 있어야 한다. 댓글에게는 저자가 필수(Mandatory)이다. 관계선에서 저자 쪽에 작대기가 그어져 있다.
    - ERD 관계선을 그릴 때 좋은 이고잉님이 만드신 프로그램 [링크](http://erd.yah.ac)
  - 나의 최종 결과물
    - ![ERD](https://github.com/sounmind/TIL/blob/master/images/2020-09-30-ERD.png?raw=true)

### 3. 논리적 데이터 모델링

- 표로 그리기
- Mapping Rule 매핑 룰(방법론)

  - Entity → Table | Attribute → Column | Relation → PK, FK
  - [ER Master](http://ermaster.sourceforge.net/) 도구로 사용하기
  - 1대1 관계(저자, 휴면저자) 일 때, 부모 테이블(PK), 자식 테이블로(FK) 설정하면 좋다.
    - ![ERM](https://github.com/sounmind/TIL/blob/master/images/2020-09-30-ERM.png?raw=true)

- 정규화
  - 단계별로 정규화 시킨다.
  - 제 1 정규화 | Atomic Columns | 컬럼 내용은 하나의 요소만 가지고 있어야 한다.
  - 제 2 정규화 | No Partial Dependencies | 부분 종속성이 없어야 한다.
  - 제 3 정규화 | No Transitive dependencies | 이행적(전이) 종속성

### 4. 물리적 데이터 모델링

---

- 실제 데이터베이스 제품에 코드를 작성해 실제로 만들기

> 이상적인 표를 구체적인 제품에 맞는 현실적인 표로 만드는 것. 이 때 중요한 것은 성능이다.

- FIND SLOW QUERY
  - 느린 성능을 보이는 쿼리를 찾는 방법이 제품마다 다르다.
- 최후의 보루 → 역정규화, 반정규화
- index 읽기 성능을 향상시키지만 쓰기 성능은 감소
- application 영역에서 캐시(cache, 저장) 시도
  - 미리 저장해둔 결과를 사용하며 데이터베이스의 부하 줄이기
- denormalization 역정규화

---

# 역정규화

---

> 정규화 → 편하게 쓰기 위해 불편하게 읽는 과정

- 엄밀한 공정이 아니다. 상황에 맞춰 적용하면 됨.

1. 컬럼의 역정규화 - Join을 줄이기
2. 컬럼의 역정규화 - 계산을 줄이기
3. 표를 쪼개기
4. 관계의 역정규화 → 컬럼을 추가하기
