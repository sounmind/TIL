# [노마드코더 | 유튜브 클론 코딩 챌린지](https://nomadcoders.co/c/wetube-challenge/lobby)

[6주 과정 진도표](https://nomadcoders.co/faq/schedule-youtube) | 2020-9-14 ~ 2020-10-23

---

# TIL | 챌린지를 진행하며 내가 한 것과 배운 것 | 3주차

# 20-09-28 | ~ #3.4 | 강의 듣고 퀴즈

---

1. 컨트롤러에서, `/user/:id`와 같은 라우트의 ID는
   - `req.params.id` 를 사용해 얻을 수 있다.
2. 컨트롤러에서 `/user?id=123`와 같은 라우트의 ID는
   - `req.query.id`를 사용해 얻을 수 있다.
3. Form 에서 POST와 GET 메소드 차이 알기
4. MongoDB의 특징에 대해 알기
5. Mongo와 Mongoosejs의 차이 알기
6. dotenv가 무엇이며 왜 사용하는지 알기
7. Schema는 무엇인가
8. Mongo는 데이터를 어떻게, 어떤 형식으로 저장하는가?
9. 다른 모델의 데이터를 어떻게 저장할 것인가?
10. `함수 이름`과 `함수 이름()`의 차이
11. Mongoose에게 특정 스키마의 모델을 만들었다고 선언하고, export하고, 첫 시작할 때 DB를 연결하는 과정 이해

### #3.0 | MongoDB

---

- mongoDB 다운로드
  - noSQL
    - 규칙이 적고 유연해서 많은 부분을 수정할 수 있다.
- mongoDB adapter → mongoosejs 다운로드

### #3.1 | Connecting to MongoDB

---

- dotenv 설치 ( 묻지도 따지지도 말고)
  - DB를 숨기고 싶을 때
- db.js 다 지우고 mongoDB 연결하기
- videoController에서 db.js import 하는 것 지우기

### #3.2 | Configuring Dot Env

---

- .env 파일을 만들고 그곳에 숨기고 싶은 키나 정보를 저장
- 키를 쓰고 싶은 js 파일에서 import 한 다음, `process.env.<변수이름>`으로 끌어다 쓸 수 있다.

  ```jsx
  import dotenv from "dotenv";
  dotenv.config();
  const PORT = process.env.PORT || 4000;
  ```

### #3.3 | Video Model

---

- Model 폴더를 만들고 그 안에 Video.js 파일 만들기
  - VideoSchema 작성
    - [Mongoose 스키마 정의 공식 문서](https://mongoosejs.com/docs/guide.html#definition)

### #3.4 | Comment Model

---

- /Model/Comment.js 파일 만들고 CommentSchema 작성하기
- Comment와 Video를 어떻게 연결할 것인가?
  1. Comment에 Video ID 연결하기
  2. Video에 Comment ID 연결하기

```jsx
// Models/Video.js
import mongoose from "mongoose";

const VideoSchema = new mongoose.Schema({
  fileUrl: {
    type: String,
    required: "File URL is required",
  },
  title: {
    type: String,
    required: "Title is required",
  },
  description: String,
  views: {
    type: Number,
    default: 0,
  },
  createAt: {
    type: Date,
    default: Date.now,
  },
  // 비디오-댓글 연결 첫번째 방법
  // video: 1, // 비디오 ID

  // 비디오-댓글 연결 두번째 방법
  comments: [
    {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Comment",
    },
  ],
});

const model = mongoose.model("Video", VideoSchema);
export default model;
```

```jsx
// Models/Comment.js
import mongoose from "mongoose";

const CommentSchema = new mongoose.Schema({
  text: {
    type: String,
    required: "Text is required",
  },
  createAt: {
    type: Date,
    default: Date.now,
  },

  // 비디오 댓글 연결 첫번째 방법
  // video: {
  //     type: mongoose.Schema.Types.ObjectId,
  //     ref: "Video"
  // }
});

const model = mongoose.model("Comment", CommentSchema);
export default model;
```

- init.js에 comment 모델 import 하기

# 20-09-29 | 코드 챌린지 | Forms and Redirects

---

- 알아야 했던 것

  - FORM 지식
    - [textarea](https://www.codingfactory.net/11611)
  - 문자열 쪼개기 [split()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/split)
  - 컨트롤러 함수 작성

    ```jsx
    // movieController.js

    // other functions

    export const postAddMovie = (req, res) => {
      const {
        body: { title, synopsis, genres },
      } = req;
      const genresSplit = genres.split(",");
      const movie = {
        title: `${title}`,
        synopsis: `${synopsis}`,
        genres: genresSplit,
      };
      addMovie(movie);
      res.redirect("/");
    };
    ```

# 20-09-30 ~ 20-10-02 | ~#3.12 | 코드 챌린지

---

## 20-09-30 | 강의 듣기

---

### #3.5 | Home Controller Finished

---

- Javascript는 한 번에 여러 일을 어떻게 할 수 있을까?
- `async`, `await`
  - async 아래 await는 await 가 있는 줄의 코드가 끝날 때(오류가 생기더라도)까지 다음 코드를 실행하지 않는 것을 말한다.
- 에러 처리
  - try, catch

### #3.6 | Uploading and Creating a Video

---

> 유저가 비디오파일을 어딘가에 업로드한 다음,
> 그 파일 경로를 데이터베이스에 넣고 그 경로로 비디오를 생성한다. → 미들웨어가 중요?!

- 비디오 이외의 파일을 업로드할 수 없도록 하기
- [파일의 url을 반환하는 미들웨어 `multer`](https://github.com/expressjs/multer/blob/master/doc/README-ko.md)
  - Upload From의 enctype에 multipart/form-data를 추가해야 함
    → 'file'을 보내는 것이기 때문에 form의 encoding이 달라야 하기 때문
- middleware.js 수정
- videoRouter.js 수정
- videoController.js 수정

  - 오류 발생과 해결

    req 객체에서 원하는 요소를 받아오는 ES6 방식에서 의미가 헷갈려서 오류가 계속 발생했다.

    예를 들어, 아래와 같은 상황에서는

    ```jsx
    export const postUpload = async (req, res) => {
      const {
        body: { title: titleName, description: descriptionName },
        file: { path: pathName },
      } = req;
    ```

    - req 객체의 body 속성 안의 title 속성의 값을 `const titleName` 으로 받아온다는 의미다. 좌측은 객체의 속성의 이름이고, 우측은 그것을 쓸 수 있는 변수 혹은 상수 이름이다. (\*변수로는 선언해보지 않아서 잘 모르겠다)
    - 하지만, 아래(`path`)와 같이 title 속성의 값만 쓰고 다른 곳에서 재사용 할 수 있다. 이 때 **newVideo의 fileUrl**에는 **req 객체의 file 속성의 path 속성의 값이 대입된다!**

    ```jsx
    export const postUpload = async (req, res) => {
      console.log(req);
      const {
        body: { title: title, description: description },
        file: { path },
      } = req;

      // 비디오 데이터베이스에 데이터 추가
      const newVideo = await Video.create({
        fileUrl: path,
        title,
        description,
      });
    ```

### #3.7 | Uploading and Creating a Video part Two

---

- videos 폴더 삭제
- mongoDB 서버를 실행시켜 videos 에 있는 데이터 삭제
- multer 미들웨어 경로 수정 → uploads/videos
- 서버 실행 → 오류 발생 → 왜? uploads/ 경로를 다룰 라우터가 없기 때문
- app.js에 미들웨어를 추가한다.

  ```jsx
  app.use("/uploads", express.static("uploads"));
  ```

  - app.use("/uploads", express.static("uploads"));
  - static() 이란? → 주어진 경로에 파일을 확인하고 serve하는 미들웨어 함수를 만든다.

    var e.static: (root: string, options?: serveStatic.ServeStaticOptions) => Handler

    **Create a new middleware function to serve files from within a given root directory**. The file to serve will be determined by combining req.url with the provided root directory. When a file is not found, instead of sending a 404 response, this module will instead call next() to move on to the next middleware, allowing for stacking and fall-backs.

  비디오가 계속 안 나오길래 파일을 분석했다.
  home.pug파일에서 mixins/videoBlock.pug에 videoFile 키로 videoFile 값을 넣어주고 있었는데 오류가 안 나고 있었다. 신기하다!? 그래서 키 이름과 값을 videoUrl과 videoUrl로 바꿔줬다.

  videoFile이라는 값은 upload.pug의 form에서 비디오 파일을 videoFile이라는 name으로 받아들이고 있었는데, 이것은 middlewares.js 의 uploadVideo 함수에서 사용하고 있었다.
  미들웨어를 좀 더 들여다보았다.

  - `.single(fieldname)`에 대한 설명은 [공식문서](https://github.com/expressjs/multer/blob/master/doc/README-ko.md#singlefieldname)에서 살펴볼 수 있었다

```jsx
// middlewares.js

import routes from "./routes";
import multer from "multer";

export const localsMiddleware = (req, res, next) => {
  // 생략
};

export const multerVideo = multer({ dest: "uploads/videos/" });

// single -> 하나의 파일만 업로드 할 수 있다
export const uploadVideo = multerVideo.single("videoFile"); // form에서 받아온 name
// .single(fieldname): 인자에 명시된 이름의 단수 파일을 전달 받는다. 이 파일은 req.file에 저장된다.
```

### #3.8 | Getting Video by ID

---

1. `"/:<name>"`으로 라우트에 작성하면, `req.params`으로 url에 입력된 경로를 `name`이라는 이름으로 받아들일 수 있다.

### #3.9 | Editing a Video

---

1. videoController.js 수정
2. videoDetail.pug 수정
3. routes.js 수정
4. videoRouter.js 수정

### #3.10 | Delete Video

---

> url로부터 id를 받아와서 해당 비디오를 삭제하기

### #3.11 | Installing ESLint

---

- Home 화면 비디오 최근 것이 상단에 노출되도록 정렬하기

> [ESLint](https://eslint.org/)는 무엇인가?

- JavaScript 코드에서 발견 된 문제 패턴을 식별하기위한 정적 코드 분석 도구
- ESLint를 설치하고 Prettier와 잘 호환되도록 설정하기
    - `npm install eslint`
    - [eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier) → 여기의 설명대로 설치하기
- [ ]  LF 와 CRLF는 무엇이고 어떤 차이가 있을까? → [블로그 설명](https://technote.kr/300)

    > CR, LF는 컴퓨터에서 줄바꿈을 의미하는 용어들이다.
    종이를 아래에서 위로 종이를 올려가며 썼던 옛날 타자기를 떠올리고 생각하면 좋다.

    - **CR : Carriage Return (\r) → 커서를 줄 올림 없이 줄 맨 앞으로 옮김**
    - **LF : Line Feed (\n) → 커서는 그대로 두고 줄을 올림**
    - 한 가지 방식만 사용할 수도 있고 둘 다 사용할 수 있다. 하지만 메모리 낭비를 줄이기 위해 한 가지만 쓰는 것이 선호되기도 한다.
    - 추가로 참고하면 좋은 링크 - **위키백과 | 새줄 문자**

### #3.12 | Searching Videos

---

- 정규표현식을 알자!
    - 연습할 때 좋은 사이트 | [regex101](https://regex101.com/)

    ```jsx
    // videoController.js
    export const search = async (req, res) => {
      const {
        query: { term: searchingBy },
      } = req;
      let videos = [];
      try {
        videos = await Video.find({
          title: { $regex: searchingBy, $options: "i" },
        });
      } catch (error) {
        console.log(error);
      }
      // ES6 이전의 방식: const searchingBy = req.query.term;
      res.render("search", {
        pageTitle: "Search",
        searchingBy,
        videos,
      }); // 그냥 serachingBy만 입력해줘도 Babel이 같은 의미로 해석해준다.
    };
    ```

### 챌린지하며 배운 것

---

- 기존의 것을 활용하면서 했기 때문에 강의를 잘 들었다면, 푸는 데 그리 큰 어려움은 없었다.
    - form 의 input 옵션에 대해 많이 알았다.
        1. type으로 문자의 종류를 정하고, 숫자일 경우 그 간격을 step으로 정할 수 있다.
        2. maxlength, minlength로 글자 수 제한을 할 수 있다.
    - 검색 시 GTE(이상, 같거나 큰) 조건으로 검색되어야 할 때 쓸 수 있는 옵션이 mongoose에 있었다.
        - mongoose Query find() 옵션 [https://mongoosejs.com/docs/api.html#query_Query-find](https://mongoosejs.com/docs/api.html#query_Query-find)