# [노마드코더 | 유튜브 클론 코딩 챌린지](https://nomadcoders.co/c/wetube-challenge/lobby)

[6주 과정 진도표](https://nomadcoders.co/faq/schedule-youtube) | 2020-9-14 ~ 2020-10-23

---

# TIL | 챌린지를 진행하며 내가 한 것과 배운 것 | 4주차

---

# 20-10-05 | Quiz: Webpack

---

## 강의 듣기 #4.0 ~ #4.3

---

### #4.0 Introduction to Webpack

---

- 웹팩이란 무엇인가?
  - module bundler
    - 많은 파일들을 가져와 Webpack에 주면, 그것을 완전히 호환이 되는 static 파일들로 바꿔준다.
- 웹팩 설치

  ```jsx
  npm install webpack webpack-cli
  ```

- `package.json` 파일 수정

  ```json
  "scripts": {
      "dev:server": "nodemon --exec babel-node init.js --delay 2",
      "dev:assets": "webpack"
    }
  ```

  - 이제 `npm start` 명령어를 사용하지 않는다. → `npm run dev:server`, `npm run dev:assets` 로 두 개의 다른 콘솔에서 나눠 실행시킨다.
  - `"dev:assets": "webpack"`은 `webpack.config.js`파일을 찾는다. 더 정확하게, `exported configuration object`를 찾는다.

- `webpack.config.js` 파일 생성

  명심하기: server 코드와는 연관시키지 않는다. 이것은 100% client 코드이다. 다시 말해, babel은 여기서 작동하지 않는다.

  - 작성

- assets 폴더 만들고, 그 안에 js, scss 폴더 만들기
- path
  - Node.js 기본 패키지

### #4.1 Styles with Webpack part One

---

- package.json 수정 → 환경 수동 설정
- webpack.config.js 수정 → scss 파일 찾아 css로 바꾸기, 텍스트 추출, 분리된 css 파일로 만들기
  - extract-text-webpack-plugin@next

### #4.2 Styles with Webpack part Two

---

- css-lader, postcss-loader, sass-loader 모두 설치
- postcss
  - 그 유용한 기능들!
  - autoprefixer 설치
- 오류 발생

  - 해결은 댓글을 참고했다.

    - 버전을 강의가 만들어진 시간대로 맞췄고
    - cross-env를 install 했다.

    댓글 보고 다 따라해도 안됐는데, webpack 공식 매뉴얼 보고 따라했더니 되네요.

    https://webpack.js.org/loaders/postcss-loader/#autoprefixer

    1. extract-text-webpack-plugin을 사용하기 위해 @wwxk1593님이 알려주신대로 버전 다운그레이드

    `npm install sass-loader@7.1`

    `npm install css-loader@1.0.1`

    2.@nek1717님이 올려주신 블로그 링크에 나와있는 webpack 버전으로 재설치

    `npm install webpack@4.36`⠀

    3. 원래 코드의 `options > plugins` 부분을 webpack 공식 매뉴얼 따라서

    `options > postcssOptions > plugins` 순서로 수정하니 정상적으로 빌드 됩니다.

    ```jsx
    {
    ㅤloader: "postcss-loader",
    ㅤoptions: {
    ㅤㅤpostcssOptions: {
    ㅤㅤㅤplugins() {
    ㅤㅤㅤㅤreturn [autoprefixer({ browsers: "cover 99.5%" })]
    ㅤㅤㅤ}
    ㅤㅤ}
    ㅤ}
    },
    ```

### #4.3 ES6 with Webpack

---

- `npm install @babel/polyfill` → 브라우저가 이해하지 못하는 자바스크립트 부분을 채워주는 역할
- `"dev:assets": "cross-env WEBPACK_ENV=development webpack -w"`와 같이 `-w`(watch) 를 붙이면 항상 변화를 감지한다.

### #4.3 ES6 with Webpack

---

- `npm install @babel/polyfill` → 브라우저가 이해하지 못하는 자바스크립트 부분을 채워주는 역할
- `"dev:assets": "cross-env WEBPACK_ENV=development webpack -w"`와 같이 `-w`(watch) 를 붙이면 항상 변화를 감지한다.

### 퀴즈를 풀며 배운 것

---

- **Webpack은** A module bundler이다.
- `webpack.config.js`에서 `module`의 역할은 각각 다른 파일 포맷에 대한 변환을 할 수 있도록 하는 것이다.
- 어떻게? `module`에서 `rules` 안에 `loader`를 다운로드하고 순서(아래에서부터 위로)에 맞게 작성해주면 된다.

# 20-10-06 | Code Challenge: Multer, FileSystem

---

- 입력 폼을 만들어 텍스트 파일을 입력하면 Multer로 텍스트파일을 프로젝트 폴더에 저장하고, nodejs의 [fs(파일 시스템](https://nodejs.org/docs/latest-v13.x/api/fs.html)) API를 이용해 텍스트 파일 내용을 읽어 내용을 웹페이지 화면에 표시해주면 된다.
- 배운 것
  1. multer 복습. "아, 이런 마법 같은 방법으로 파일이 저장되는 구나."
  2. 파일 시스템의 동작 원리와 경로 설정의 중요성.

# 20-10-07 | #6.0 ~ #6.5 | Quiz: 사용자 인증

---

### #6.0 Introduction to PassportJS | 사용자 인증을 위해 알아야 할 개념과 도구

---

- [Passportjs](http://www.passportjs.org/)
  - [생활코딩 | Passportjs](https://www.opentutorials.org/course/3402)
  - 여기서 `strategy`는 무엇인가?
- '쿠키'란?
  - [MDN | HTTP 쿠키](https://developer.mozilla.org/ko/docs/Web/HTTP/Cookies)
- [Passport-Local Mongoose](https://github.com/saintedlama/passport-local-mongoose)

### #6.1 Local Authentication with Passport part One

---

- passport-local-mongoose 설치
- models/User.js 작성
- init.js 에 작성한 Schema를 Import
- passport passport-local 설치
- ./passport.js 작성
  - passport-local-mongoose가 제공하는 strategy 사용
    - [createStrategy()](https://github.com/saintedlama/passport-local-mongoose#simplified-passportpassport-local-configuration)

### #6.2 Local Authentication with Passport part Two

---

- Serialization 에 대한 passportjs의 문서 살펴보기

  > serializeUser → 특정정보(field)를 쿠키에 담아 전달하기

  > deserializeUser → 받은 쿠키로 사용자를 특정하기

  ### Sessions

  In a typical web application, the credentials used to authenticate a user will only be transmitted during the login request. If authentication succeeds, a session will be established and maintained via a cookie set in the user's browser.

  Each subsequent request will not contain credentials, but rather the unique cookie that identifies the session. In order to support login sessions, Passport will serialize and deserialize `user` instances to and from the session.

  ```
  passport.serializeUser(function(user, done) {
    done(null, user.id);
  });

  passport.deserializeUser(function(id, done) {
    User.findById(id, function(err, user) {
      done(err, user);
    });
  });

  ```

  In this example, only the user ID is serialized to the session, keeping the amount of data stored within the session small. When subsequent requests are received, this ID is used to find the user, which will be restored to `req.user`.

  The serialization and deserialization logic is supplied by the application, allowing the application to choose an appropriate database and/or object mapper, without imposition by the authentication layer.

[passport-local-mongoose](https://github.com/saintedlama/passport-local-mongoose#configure-passportpassport-local) 에서 de/serializeUser 함수를 제공해주기 때문에 Shorcut을 이용할 수 있다.

- passport.js 작성하기
- 사용자 인증 과정을 추가하기
  - globalRouter.js 수정하기
  - userController.js 수정하기

> mongoDB에 사용자 id와 패스워드를 암호화해서 담는 것까지 완료. 아직 쿠키는 없다. 즉, 아직 로그인이 되지 않았다는 것.

### #6.3 Loggin the User In

---

- userController.js 의 postJoin 함수를 미들웨어로 탈바꿈시키기
- globalRouter에서 postJoin 다음에 postLogin을 작성
- useController.js 에서 postLogin 작성

  > 공식 문서 참고!

  ## Redirects

  A redirect is commonly issued after authenticating a request.

  ```
  app.post('/login',
    passport.authenticate('local', { successRedirect: '/',
                                     failureRedirect: '/login' }));

  ```

  In this case, the redirect options override the default behavior. Upon successful authentication, the user will be redirected to the home page. If authentication fails, the user will be redirected back to the login page for another attempt.

> postJoin은 이메일, 패스워드 등의 정보들을 받아 사용자를 가입시키고, postLogin은 같은 정보를 가지고 사용자를 로그인 시킨다.

- app.js 에서 각종 사용자 인증 관련 모듈 import

  ```jsx
  import express from "express";
  import morgan from "morgan";
  import helmet from "helmet";
  import cookieParser from "cookie-parser";
  import bodyParser from "body-parser"; // 이게 있어야 req 객체를 읽어들일 수 있음
  import passport from "passport";
  import "./passport";
  import { localsMiddleware } from "./middlewares";
  import userRouter from "./routers/userRouter";
  import videoRouter from "./routers/videoRouter";
  import globalRouter from "./routers/globalRouter";
  import routes from "./routes";

  const app = express();

  app.use(helmet({ contentSecurityPolicy: false })); // 보안 약화
  app.set("view engine", "pug"); // view

  app.use("/static", express.static("static"));
  app.use("/uploads", express.static("uploads")); // 프로젝트 안의 uploads 폴더를 찾아 파일 확인하는 미들웨어
  app.use(cookieParser());
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));

  app.use(morgan("dev"));

  app.use(passport.initialize()); // passport 실행
  app.use(passport.session()); // 쿠키 정보에 해당하는 사용자 찾기 // 아직 세션 모듈을 설치하지 않았다.

  app.use(localsMiddleware);

  app.use(routes.home, globalRouter);
  app.use(routes.users, userRouter);
  app.use(routes.videos, videoRouter);

  export default app;
  ```

### #6.4 Sessions on Express

---

- [express-session 설치](https://www.npmjs.com/package/express-session)
- [세션은 무엇인가?](https://developer.mozilla.org/en-US/docs/Web/HTTP/Session)

  > 세션이란 일정 시간동안 같은 사용자(정확하게 브라우저를 말한다)로 부터 들어오는 일련의 요구를 하나의 상태로 보고 그 상태를 일정하게 유지시키는 기술이라고 한다. 또한 여기서 일정 시간이란 방문자가 웹 브라우저를 통해 웹 서버에 접속한 시점으로부터 웹 브라우저를 종료함으로써 연결을 끝내는 시점을 말하며 즉, 방문자가 웹서버에 접속해 있는 상태를 하나의 단위로 보고 세션이라고 칭한다. [출처](https://88240.tistory.com/190)

- app.js에 express-session import 하고 미들웨어로 선언.

  - 옵션

    - secret

      - 암호화를 위한 무작위 문자열을 가져와서, `.env`파일에 선언해둔다.
      - env 파일을 import 한다.

        ```jsx
        import dotenv from "dotenv";
        // ...
        dotenv.config();
        ```

    - resave
    - saveUninitialized

  - isAuthenticated 옵션이 이제 없으므로 header.pug 수정
  - 테스트 후 문제 확인
    - 서버에서 코드 수정 후 재시작하면 현재 로그인 된 사용자의 세션이 사라지는 상황. 세션을 사라지지 않도록 해야 함.

### #6.5 MongoStore and Middlewares

---

- [connect-mongo 설치](https://www.npmjs.com/package/connect-mongo)
- app.js 에서

  - mongoose, connect-mongo를 import

  ```jsx
  const CookieStore = MongoStore(session);
  // ...
  app.use(
    session({
      secret: process.env.COOKIE_SECRET,
      resave: true,
      saveUninitialized: false,
      store: new CookieStore({
        mongooseConnection: mongoose.connection,
      }),
    })
  );
  ```

- 라우트 관리
  - 이미 로그인 된 사용자는 Join 화면으로 접근하지 못하게 하기
  - 미들웨어를 추가해서 컨트롤러에 적절하게 넣어주면 된다.

### 퀴즈

---

강의를 열심히 들었다면 무난하게 풀 수 있었던 문제들이었다.

# 20-10-08 | Code Challenge | request.js, HTTP Status Code

---

- 필요 개념
  - [request](https://www.npmjs.com/package/request#super-simple-to-use) 패키지
  - [HTTP Status Code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
  - [`toLowerCase()`](https://opentutorials.org/course/50/99)
  - [`indexOf()`](https://opentutorials.org/course/50/89)
- 웹페이지 url 경로에 query로 다른 웹사이트 url를 입력했을 때 해당 url의 서버의 상태를 확인하는 과제이다.
  - 이전 파이썬웹스크래퍼에서도 비슷한 내용의 과제가 있어 쉽게 해결했다.
  - url에 http가 포함되어 있지 않으면 앞쪽에 `http://`를 추가해줬다.

# 20-10-09 | 강의 듣기 | #6.6 ~ #6.12

### #6.6 ~ 6.8 Github Log In

---

- passport-github 설치
- 오류 발생

  > NodeJS address already in use 문제 → 해당 포트를 이미 사용중이다.

  - 서버 실행하는 데 오류가 발생해서 구글링했다.
  - NodeJS 프로세스가 이전에 비정상적으로 종료됐을 때 나타나는 에러 메시지였다.
  - [여기 블로그 포스팅](https://jootc.com/p/201912253249)을 참고하여 해결했다.

- [passport-github strategy 공식문서](http://www.passportjs.org/packages/passport-github/)를 참고해 진행한다.
- 인증까지 성공한다면,
  - userController.js에서 githubLoginCallback 함수 작성
- 테스트 중 오류 발생

  > Error: Failed to serialize user into session

  - [해결방법1](https://moollang.tistory.com/35) → 이메일이 private이기 때문에 public으로 바꿔줘야 함.
    - 하지만 다른 웹사이트에서, 나는 이제까지 private 상태로 잘 가입했었는데 이상하다?!
  - 해결방법2 → passport.js 의 `serializeUser()` 함수의 인자에 `function (user, done) { done(null, user);` 을 추가 작성한다. → 이유는 아직 모른다 ... 찾아 볼 것!!!

  ```jsx
  passport.serializeUser(function (user, done) {
    done(null, user); // 왜 이렇게 하면 github session serialize 오류가 해결되는 것일까?
  });

  passport.deserializeUser(function (user, done) {
    done(null, user);
  });
  ```

- **serialize 와 deserialize 과정을 잘 이해해야 한다.**
  - 이 [링크](https://stackoverflow.com/questions/27637609/understanding-passport-serialize-deserialize)를 참고하자.

### #6.9 Recap | 잠 깐 만 ~

---

- 깃허브 인증 과정 정리
  1. 깃허브 버튼 클릭 → 사용자가 깃허브 웹사이트로 이동
  2. 권한 승인 버튼 클릭 → 깃허브는 /auth/github/callback 라는 경로(passport.js의 GithubStrategy에 callbackURL로 설정)로 사용자의 정보를 보내준다.
  3. 그렇게 되면, passportjs가 함수를 호출한다. 개발자가 사전에 설정하고 만든 함수(passport.js 의 GithubStrategy에 호출하라고 되어 있는 githubLoginCallback )이다. 이 함수의 인자로 깃허브에 등록되어 있는 사용자의 모든 정보를 받는다.
  4. githubLoginCallback 함수는 callback(cb) 함수를 리턴해야 한다. 그 함수(cb)의 첫번째 인자는 error가 있는지 없는지 여부이고, 두번째 인자는 유저가 있는지 여부이다.
     - 에러가 존재하거나 user가 없으면 passport는 user가 없다고 판단하고 로그인 과정을 중단한다.
     - 에러가 없고 user가 있으면 passport는
       1. user 정보를 받아 쿠키를 만든다.
       2. 그 쿠키를 저장한다.
       3. 그 저장된 쿠키를 브라우저로 보낸다.
       4. 마지막으로 홈페이지로 redirect 된다. ( 로그인 완료 )

### #6.9 User Profile | [출처 명확한 user를 찾아...](https://github.com/sounmind/youtube-clone-coding/commit/0e732380c431fb2f73ba335c04fc389df2119a7e)

---

- userDetail 에서는 특정 id를 가진 (로그인 된) 사용자를 찾아야 한다.
  - /users/\${id} 보다 /users/me 로 하는 게 낫다. 왜?
    - 사용자마다 똑같은 user template을 사용하는데, userDetail 컨트롤러 함수에서 사용자를 찾게 하기 싫어서... → **무슨 말인지 모르겠다!!!!**
  - routes.js 에 `/me` 경로 추가, globalRouter에 미들웨어 추가, userController에 getMe 함수 추가
  - middlewares.js 에서 `res.locals.user` → `res.locals.loggedUser` 로 변경 → user 정보를 어떻게 얻은 것인지 좀 더 명확해지도록 변경
  - header.pug 에서 profile로 가는 링크 `/me` 로 변경

### #6.10 User Detail

---

- /me 로만 프로필 정보에 접근할 수 있었는데, /users/:id 경로로도 프로필 페이지로 접근할 수 있도록 컨트롤러 함수를 수정했다.

```jsx
export const userDetail = async (req, res) => {
  const {
    params: { id }, // users/:id 의 id를 받는다.
  } = req;
  try {
    const user = await User.findById(id); // id에 해당하는 user를 찾아서 userDetail 페이지에 전달한다.
    res.render("userDetail", { pageTitle: "User Detail", user });
  } catch (error) {
    console.log(error);
    res.redirect(routes.home);
  }
};
```

### #6.10 Facebook Login Part One

---

- 페이스북 인증은 강사가 어렵다고 하고, 시간도 새벽 3시 43분이라 늦었다.
- 직접 타이핑 말고 한 번 쓱 전체 과정을 훑어보자.
- 내일 다시 시청-실습-정리하면서 학습하자.
