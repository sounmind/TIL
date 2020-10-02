# [노마드코더 | 유튜브 클론 코딩 챌린지](https://nomadcoders.co/c/wetube-challenge/lobby)

[6주 과정 진도표](https://nomadcoders.co/faq/schedule-youtube) | 2020-9-14 ~ 2020-10-23

---

# TIL | 챌린지를 진행하며 내가 한 것과 배운 것 | 2주차

# 20-09-21 | 코드 챌린지 | Pug, fontawesome, res.locals, render()

---

### 이전부터 나를 괴롭혔던 오류를 고쳐보자...(결국 실패)

---

fontawesome을 링크(css, js)로 불러와지지 않는 오류가 있었다. 구글의 콘텐츠 보안정책이라고 하는데... 아래와 같은 오류 메시지가 뜬다.

```jsx
Refused to load the script 'https://kit.fontawesome.com/*ID*.js' because it violates the following Content Security Policy directive: "script-src 'self'". Note that 'script-src-elem' was not explicitly set, so 'script-src' is used as a fallback.
```

- 따라서 [구글의 콘텐츠 보안정책 문서](https://developers.google.com/web/fundamentals/security/csp?hl=ko)를 읽어보고 이 문제를 해결할 수 없나? ( 내가 판단하기에 신뢰할 수 있는 사이트, 스크립트 소스이니까 허용해줘! 를 어떻게 알리나 ) 생각해봤다.
- 결론 → 해결하지 못했다. 아무리 연구해봐도 아이콘이 제대로 나타나지 않고 보안정책 오류가 계속 나온다..ㅠㅠ 일단 여기에 시간이 너무 지체되면 안되니까 그냥 무시하고 진도를 나가도록 하자.

### middleware를 만들고 그 안에서 [res.locals](https://expressjs.com/ko/api.html#res.locals)에 변수를 선언-저장하면 그 변수들을 template에서 쓸 수 있다.

---

```jsx
// middlewares.js
import routes from "./routes";

export const localsMiddleware = (req, res, next) => {
  res.locals.siteName = "WeTube"; // title에 이 변수를 쓸 수 있다.
  res.locals.routes = routes; // partials/header에서 링크에 routes를 변수처럼 쓸 수 있다.
  next();
};
```

### [render 함수](https://expressjs.com/ko/api.html#res.render)의 첫번째 인자는 템플릿, 두번째 인자는 템플릿에 추가할 정보가 담긴 객체다.

---

```jsx
// userController.js
export const join = (req, res) => res.render("join", { pageTitle: "Join" });
export const login = (req, res) => res.render("login", { pageTitle: "Log In" });
export const logout = (req, res) =>
  res.render("logout", { pageTitle: "Log Out" });
export const userDetail = (req, res) =>
  res.render("userDetail", { pageTitle: "User Detail" });
export const editProfile = (req, res) =>
  res.render("editProfile", { pageTitle: "Edit Profile" });
export const changePassword = (req, res) =>
  res.render("changePassword", { pageTitle: "Change Password" });
```

## 오늘 과제의 교훈

---

- 난이도는 쉬웠다. 강의 내용을 그대로 복습하고 재생산하는 정도였다. 웹 페이지 구현의 흐름을 어렴풋이 파악할 수 있었다.
- fontawesome과 구글보안정책은 ... 도저히 어떻게 해야할지 모르겠다. 나중에 슬랙 커뮤니티에 질문을 해봐야겠다.

# 20-09-22 | 퀴즈 | middleware, route, router, MVC pattern

---

- middleware(미들웨어), route(라우트), router(라우터), MVC pattern 개념을 복습했다.
  1. middleware는 3개의 함수 인자, request, response, next를 가진다
     1. request는 url로부터 들어온 정보를 다룬다. response는 서버가 클라이언트로 전송하는 내용을 다룬다. `next()`는 다음 middleware를 호출한다.
  2. 라우트들은 곧 미들웨어이다. `response.end()`로 연결을 끊을 수 있다.
  3. `app.use(<ROUTER>)`으로 해당 라우터를 어플리케이션에서 사용할 수 있다.
  4. `app.get()`은 GET requests에 의해 호출되고 `app.use()`는 모든 requests에 의해 호출된다.
  5. MVC는 Model View Controller를 뜻하는 디자인 패턴이다. 모델은 데이터를 저장하고 뷰는 사용자가 실제로 보는 것이고, 컨트롤러는 웹페이지 내부 로직을 담당한다.

# 20-09-23 | 퀴즈

---

- express가 pug를 사용하도록 하기 ( 선언, 디렉토리 설정, 렌더링)

### 선언

---

- `app.set("view engine", "pug")`
- `app.set("views", "/myDirectory")` → 커스텀 디렉토리 설정
- `res.render(<Template_name>)` → render()함수에 첫번째 인자로 템플릿인 pug 파일 이름을 넣어주면 된다.

  - `res.render(<Template_name>, {name: "<Your_name>"})` → 컨트롤러에서 렌더링할 때 두번째 인자로 변수이름을 선언하고 값을 대입할 수 있다.

    ```jsx
    // userController.js
    export const join = (req, res) => res.render("join", { pageTitle: "Join" });
    export const login = (req, res) =>
      res.render("login", { pageTitle: "Log In" });
    export const logout = (req, res) =>
      res.render("logout", { pageTitle: "Log Out" });
    export const userDetail = (req, res) =>
      res.render("userDetail", { pageTitle: "User Detail" });
    export const editProfile = (req, res) =>
      res.render("editProfile", { pageTitle: "Edit Profile" });
    export const changePassword = (req, res) =>
      res.render("changePassword", { pageTitle: "Change Password" });
    ```

### 디렉토리 설정

---

- `/views` → pug 파일들이 들어가는 디렉토리 ( 현재 디폴트로 설정된 폴더)
  - `/layouts` → 레이아웃 폴더,
    - `main.pug` → 메인 페이지로 쓸 html 파일
  - `/partials` → 재사용이 많이 되는 html의 일부분
    - `footer.pug`
    - `header.pug`
  - 기타 다른 페이지의 pug 파일들 ( login.pug, home.pug, deleteVideo.pug ... )

### pug의 편리한 html tag 사용법

---

- `<span class="className">` == `span.hello`
- `<div class="className"></div>`==`div.hello`==`.hello`
- `middlewares.js`

  ```jsx
  import routes from "./routes";

  export const localsMiddleware = (req, res, next) => {
    res.locals.siteName = "WeTube"; // title에 이 변수를 쓸 수 있다.
    res.locals.routes = routes; // partials/header에서 링크에 routes를 변수처럼 쓸 수 있다.
    next();
  };
  ```

# 20-09-24 ~ 20-09-25 | 코드 챌린지

---

## 20-09-24 | 강의 듣기 (~#2.20)

---

### #2.18 | Search Controller

---

1. views

   - form을 만들어 사용자의 입력 정보를 get method로 정보를 정해진 url로 보낸다.

   ```html
   .header__column form(action=routes.search, method="get")
   <!-- 폼을 제출하면 get 방식으로 정보를 가진채 routes.search로 url 이동. /search?term=<somethingYouTyped> -->
   input(type="text", placeholder="Search by term...", name="term")
   ```

2. controller

   - controller가 query에 접근하려면 method가 get이어야 한다.
   - request 객체에서 내가 원하는 요소를 찾는다.

     ```jsx
     export const search = (req, res) => {
       const {
         query: { term: searchingBy },
       } = req; // ES6 이전의 방식: const searchingBy = req.query.term;
       res.render("search", { pageTitle: "Search", searchingBy: searchingBy }); // 그냥 serachingBy만 입력해줘도 Babel이 같은 의미로 해석해준다.
     };
     ```

   - 그것을 랜더링 한다.

3. views

   - 출력 결과를 사용자에게 보여준다.

   ```html
   extends layouts/main block content .search_header h3 Searching by
   #{searchingBy}
   <!-- 이것이 보이려면 컨트롤러를 수정해야 함 -->
   ```

### #2.19 | Join, Log In HTML

---

- pug 에서 띄워 쓴 텍스트를 작성할 때 첫 단어를 태그로 취급하므로 `|`를 앞에 써줘서 `|`뒤가 텍스트라는 것을 알려줄 수 있다.

### #2.20 | Change Profile HTML

---

- edit-profile , id 인식 오류

## 20-09-25 | 강의 듣기(~#2.25)

---

### #2.21 | Home Controller

---

1. fake db (비디오 정보의 배열)를 만들고 export 한 다음
2. video controller로 배열을 전달했다.
3. home.pug 템플릿에서 each in 함수를 써서 배열을 반복 출력했다.

   - `h1=`, `p=`처럼 `=`을 붙여 써줘야 한다.

     ```html
     extends layouts/main block content .videos each video in videos h1=
     video.title p= video.description
     ```

### #2.22 | Home Controller Part Two | mixin: 웹사이트에서 반복되는 html를 재사용하기

---

- 목표: home에서도 비디오가 보이고, 누군가의 profile에서도 그 비디오를 볼 수 있어야 한다.
- mixin은 pug 함수의 일종

> 또, CSP 이슈가 터졌다... 개 같은 거

코멘트를 읽어보자.

> 미디어 소스나 폰트어썸 사용 안되시는 분들이 많은 것 같은데 앞서 추가했던 helmet의 미들웨어 중에 helmet.contentSecurityPolicy()이 원인이 되는 것 같습니다. 과거에는 app.use(helmet())을 사용할 경우 기본적인 보안설정만 해주었는데 현재는 csp설정도 포함되어 이러한 문제가 발생하는 것 같습니다.
> 참조 링크:
> [https://www.npmjs.com/package/helmet](https://www.npmjs.com/package/helmet)
> [https://7stocks.tistory.com/94](https://7stocks.tistory.com/94)
> [https://www.npmjs.com/package/helmet-csp](https://www.npmjs.com/package/helmet-csp)

> 밑에 @luceverus 님 댓글 덕분에 저도 찾아봤는데, 우리가 미들웨어어 넣어놓은 helmet 에서 contentSecurityPolicy()를 해놔서 동영상이 안나오는것 같아요.
> 그래서 찾아보니까
> app.use(helmet()); 에서
> app.use( helmet({ contentSecurityPolicy: false, })); 로 설정 하면 contentSecurityPolicy만 끌 수 있어요. 당분간 이렇게 쓰시고 나중에는 보안을 위해서 다시 app.use(helmet());로 하는게 좋을듯 해요.

### #2.23 | Join Controller

---

> 로직 → 누군가가 회원가입을 하면 자동으로 Login이 된 상태로 Home 화면으로 이동하고 싶다.

1. userController의 join 함수 변경 → getJoin, postJoin 으로 분리

   - /join 경로로 POST 하기 위한 설정이나 코드가 아직 없기 때문.
   - Join form을 작성하면 post 방식으로 받아 들이도록 한다.
     - 라우터와 컨트롤러를 적절히 변경한다.

   ```jsx
   // globalRouter.js
   import express from "express";
   import routes from "../routes";
   import { home, search } from "../controllers/videoController";
   import {
     getJoin,
     postJoin,
     login,
     logout,
   } from "../controllers/userController";

   const globalRouter = express.Router();

   globalRouter.get(routes.join, getJoin);
   globalRouter.post(routes.join, postJoin);
   ```

   ```jsx
   // userController.js
   import routes from "../routes";

   export const getJoin = (req, res) => {
     res.render("join", { pageTitle: "Join" });
   };
   export const postJoin = (req, res) => {
     const {
       body: { name, email, password, passwordV },
     } = req;

     // 비밀번호 체크
     if (password != passwordV) {
       res.status(400); // 잘못된 요청이라는 상태 코드 전달
       res.render("join", { pageTitle: "Join" });
     } else {
       // To Do: Register User 유저 등록
       // To Do: Log User In 로그인 된 채로 home 접속
       res.redirect(routes.home);
     }
   };
   ```

- 상태 코드status code → 웹 사이트가 이해할 수 있는 코드

### #2.24 | Log In and User Profile Controller

---

1. login도 postLogin과 getLogin으로 분리
2. middleware.js에서 로그인 여부를 확인하기 위한 fake data 추가
3. header.pug 변경

   - 로그인이 확인되면, upload, profile, log out 이 나타나도록 수정

   > profile을 클릭했을 때 `/:id`로 가는 경로에 문제가 있다.

   > express는 저 `:id`를 id라는 변수에 있는 값을 대입하는 것으로 '잘' 이해하지만 html 은 그렇지 않다!

   - routes.js의 userDetail을 함수로 바꾼다.
   - userRouter.js에서 userDetail을 위에서 바꾼대로 변경해준다. 함수가 실제로 실행되어 id 값을 리턴해야 된다.
   - 하지만 템플릿에서는 인자 없이 실행되면 안 된다. user.id를 인자로 입력해야 한다.
     - header.pug 변경
   - 경로에 id가 들어가 있는 videoDetail도 수정해야 한다.
     - routes.js에서 routes 객체에서 videoDetail을 함수로 만들어주기

### #2.25 | More Controllers ( video detail, logout, upload )

---

> 비디오를 클릭하면 비디오 상세 설명 페이지로 이동하도록 하고 싶다.

- videoBlock.pug에서 mixin 안의 내용을 수행한다. 비디오 제목과 조회수를 클릭하면 비디오 상세페이지로 가도록 링크를 만든다.
  - 라우트를 써줄 때 videoDetail의 경우 함수이니 videoDetail()처럼 괄호를 붙여줘야 하고 템플릿에서는 함수에 인자가 필요하므로 인자를 넣어준다. videoDetail(video.id)
  - id를 받도록 home.pug에서도 id를 적어준다.
- 오류가 생겼는데, videoRouter에서 route를 적어줄 때 괄호를 적어주지 않아 함수로 취급이 안되어서 그렇다.

> log out

- 로그아웃 프로세싱은 나중으로 미루고
- home으로 리다이렉트 시키도록 작성

> upload

- 기존 경로는 /upload인데, /videos/upload로 가야한다.
- header.pug에서 수정
- upload.pug 수정
  - getUpload와 postUpload로 분리
- videoController.js 수정
  - postUpload 함수가 특정(임의로 fakeDB에 있는 id값 입력) id의 videoDetail 페이지로 리다이렉트
- videoRouter.js 수정

> 폼 입력에 required=true 추가

## 20-09-24 ~ 25 코드 챌린지

---

- 필요했던 개념
  - 서버 동작 방식, 특히 컨트롤러
  - PUG 와 Mixin
  - GET, POST 요청에서 어떻게 원하는 내용을 추출할 것인가
  - API 함수 불러온 것 이해하고 사용하기
  - 방대한 JSON 데이터 자료에서 원하는 내용을 어떻게 추출할 것인가
