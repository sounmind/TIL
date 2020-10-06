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