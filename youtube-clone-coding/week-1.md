# [노마드코더 | 유튜브 클론 코딩 챌린지](https://nomadcoders.co/c/wetube-challenge/lobby)

[6주 과정 진도표](https://nomadcoders.co/faq/schedule-youtube) | 2020-9-14 ~ 2020-10-23

---

# TIL | 챌린지를 진행하며 내가 한 것과 배운 것 | 1주차

---

# 20-09-17 | 코드 챌린지 | Making Express Server, Handling Routes, Middleware

---

1. [node.js 다운로드](https://nodejs.org/ko/) → 자동으로 npm이 다운로드 된다
2. ([**npm 다운로드**](https://www.npmjs.com/))
3. 라우트들을 통제하기
   1. [\*\*자바스크립트 컴파일러 Babel](https://babeljs.io/docs/en/)\*\* 다운로드
   2. 자바스크립트 **[arrow function(화살표 함수)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/%EC%95%A0%EB%A1%9C%EC%9A%B0_%ED%8E%91%EC%85%98)** 사용해보기
   3. 새로 저장할 때마다 자동으로 어플리케이션을 재시작시켜주는 node.js 패키지 **[nodemon 설치](https://www.npmjs.com/package/nodemon)**
      - 설치할 때 devDependencies로 설치하기 → 패키지에 꼭 필요한 것이 아니라, 개발자에게 필요한 것이기 때문에 `npm install nodemon -D`로 설치하면 된다.
      - 바로 재시작을 하면 Babel이 컴파일할 시간이 없기 때문에 재시작 지연 시간을 2초로 두면 좋다.
4. [**npm으로 express 다운로드**](https://www.npmjs.com/package/express)
5. 나만의 express 서버 만들기
6. 미들웨어 만들기
   1. 로깅(logging)을 도와주는 **[Morgan 이라는 미들웨어](https://www.npmjs.com/package/morgan) 설치**
   2. 보안을 위한 미들웨어, **[Helmet](https://www.npmjs.com/package/helmet) 설치**
   3. request 객체에 접근하기 위한 미들웨어
      1. 유저 정보를 다루기 위한 [cookie parser 쿠키파서](http://expressjs.com/en/resources/middleware/cookie-parser.html)
      2. form 정보를 다루기 위한 [body parser 바디파서](http://expressjs.com/en/resources/middleware/body-parser.html)
7. 리다이렉트 하기

- 참고한 express 공식 문서
  1. 라우트(Route)를 받는 app.get()에 대해 알아보자 → [**app.get()**](https://expressjs.com/ko/4x/api.html#app.get)
  2. 미들웨어에 대해 더 알아보자 → [\*\*미들웨어 사용](https://expressjs.com/ko/guide/using-middleware.html) | [app.use](https://expressjs.com/ko/api.html#app.use)\*\*
  3. Response 객체엔 뭐가 있을까? **[Response](https://expressjs.com/ko/4x/api.html#res)**
     - **[res.send()](https://expressjs.com/ko/4x/api.html#res.send)**
  4. 왔어요? 돌아가셔요. → [res.redirect()](http://expressjs.com/ko/api.html#res.redirect)
- 추후에 할 것
  1. package.json 분석하기

# 20-09-18 | 코드 챌린지 | Routing, MVC Pattern,

---

## 내용

---

1. Javascirpt ES6 모듈 module 사용
2. Router

   > 라우팅은 URI(또는 경로) 및 특정한 HTTP 요청 메소드(GET, POST 등)인 특정 엔드포인트에 대한 클라이언트 요청에 애플리케이션이 응답하는 방법을 결정하는 것을 말합니다.

   - **[기본 라우팅 소개](https://expressjs.com/ko/starter/basic-routing.html)**

   > route들의 복잡함을 쪼개주기 위해 사용

   - Express [라우팅](https://expressjs.com/ko/guide/routing.html)
     - 클론코딩에서 ~router.js 에서 사용한 클래스

3. MVC Pattern

   [웹 개발 위한 기본 지식](https://www.notion.so/183a62819db842e78b00de8c205aed90)

4. 강사가 좋아하는 분할 정복 방법이란?

> Divide and Conquer

- 분할 정복법은 [알고리즘](https://ko.wikipedia.org/wiki/%EB%B6%84%ED%95%A0_%EC%A0%95%EB%B3%B5_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)으로 유명하다.
- 원리는 다음과 같다.

  > 해결하기 어려운 문제를 작은 문제로 분할하여 (그것을 하나씩 정복하여) 문제를 해결한다.

  - 위의 원리는 알고리즘 문제를 풀 때 더 직관적으로 다가온다. 웹 사이트나 서버를 개발할 때는 다음과 같은 원칙으로 변환해 받아들이면 좋겠다고 생각했다.
    - 하나의 함수에 하나의 기능만 구현한다.
    - 커다란 기능의 집합인 웹사이트를 상상한다. 그 통합적 기능을 하나하나 분할한다. 그것을 이해하기 쉽게 더 이상 쪼갤 수 없는 하나의 기능으로 쪼개어 나눈다. 하나씩 구현하여 합쳐나간다. 웹 사이트를 완성시킨다.

## 오늘 과제의 교훈

---

1. **웹 페이지 구조를 이해하는 것은 정말매우몹시 중요하다.** 제대로 이해하고 있지 않으면 아무것도 할 수가 없다. 그저 나타나는 오류에 수동적으로 대응해야 한다.
   - 라우트 - 라우터 - 컨트롤러 개념을 잘 알자.
     - 예를 들어 /api 에서 v1, v2로 분기하여 여러 갈래로 형성되는 route를 가진 서버를 만들 경우. **일일히 경로를 모두 써주는 것이 아니라,** 처음 `app.use()`로 받은 경로 **뒤에 붙여서 써주는 개념이다.**
     - 소스코드

- **알고 복사-붙여넣기하자**. 컨트롤러는 라우트를 통해 들어온 요청을 처리하는 객체다. 오늘 과제에서는 간단하게 화면에 글자만 뿌려줬다. 과제 진행 시 template도 생성하지 않았는데, `res.render()`를 쓰는 바람에 오류가 났었다.
- **변수 이름 제대로 파악하고 사용하는 것은 기본**이다. 이번 과제에서 적잖이 발목 잡혔다. 라우트, 라우터, 컨트롤러 변수 이름이 너무 많아서 헷갈렸는데 그러지 않을만한 나만의 규칙이나 컨벤션을 알아놓는 게 좋겠다.
  - express convention으로 검색해보니, [패키지](https://www.npmjs.com/package/express-convention-routes)도 있다!
  - 블로그 글도 있다. [Node.js/Express Convention-Based Routes](https://blog.codewithdan.com/node-js-express-convention-based-routes/) 위 패키지의 사용 제안서 같다...?