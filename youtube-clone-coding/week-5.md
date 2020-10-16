# [노마드코더 | 유튜브 클론 코딩 챌린지](https://nomadcoders.co/c/wetube-challenge/lobby)

[6주 과정 진도표](https://nomadcoders.co/faq/schedule-youtube) | 2020-9-14 ~ 2020-10-23

---

# TIL | 챌린지를 진행하며 내가 한 것과 배운 것 | 5주차

# 20-10-12 | Code Challenge | Video Player

---

## #6.10 ~ #6.12 Facebook Login (실습 없이 정리만)

---

Facebook 로그인 절차를 수행하려면 임시 주소가 필요하기 때문에 코드를 작성하지 않고 그 방법만 알고 정리하도록 한다.

1. [developers.facebook.com](http://developers.facebook.com) 에서 애플리케이션 생성
2. Add a Product → Facebook Login → Set up → Site Url(http://localhost:4000) 입력 → next next next ... 
    - Settings에서 발급받은 ID와 Password를 프로젝트 폴더 안의 `.env` 폴더에 작성하기.
3. passportjs의 passport-facebook 설치
4. passport.js에 strategy 설정 작성
5. routes.js 에 facebook 인증을 위한 라우트 작성
6. userController.js에 콜백 함수 만들기
    1. 페이스북 페이지로 보내서 인증을 받고
    2. 가입된 유저인지 확인하고
    3. 홈페이지로 리다이렉트
7. globalRouter.js 에서 라우터 안에서 라우트 → 컨트롤러 연결
8. facebook for Developers 에서 app 설정 → Privacy Policy URL 입력 → Status: Live 상태로 바꾸기
9. 오류 발생! facebook은 http://로 오는 정보는 보안 문제 때문에 받지 않는다. 하지만 localhost는 http 주소로 시작하기 때문에 조치를 취해줘야 함.
10. localtunnel 설치하여 https:// 로 시작하는 주소(그 주소로 가면 결국 localhost로 연결되는) 생성하기
11. facebook for Developers 에서 app 설정 → app Domain에 새로 생성된 주소 넣기 또는 Valid OAuth Redirect URLs에 넣기
12. [passport-facebook strategy](http://www.passportjs.org/packages/passport-facebook/)
    - 빠진 부분 없이 구체적으로 작성
13. userController.js에서 페이스북으로부터 받아온 사용자 정보를 개발자 편의에 맞게 수정

## #7 Relationships And Route Protection

---

### ~ #7.1 Edit and Update User Profile

---

- 프로필에 자신의 정보가 출력되고 수정할 수 있어야 한다.

Oct 12, 2020 6:24 PM 오늘은 아마 여기까지

- 오류 및 문제
    - 정보를 수정한 다음 리다이렉트 되고 나서 db는 업데이트 됐으나 화면에서는 update 되지 않음.
        - User 정보가 어떻게 입력되고 수정되는지 그 과정을 심도 있게 살펴봐야 함!

### #7.2 Change Password

---

- DB와 연동하는 것은 참으로 오묘하다.
- req.user에서 바로 changePassword 함수를 쓸 수 없었다. 강사는 잘만 쓰던데 왜 나는 못 쓰는 것일까. 그렇지만 깊게 파고들 틈 없이 일단 진도를 나가야 한다. 과제를 작성해야 하기 때문이다.
- 일단 공식 문서는 [여기](https://github.com/saintedlama/passport-local-mongoose#changepasswordoldpassword-newpassword-cb) 있다.
- 문제의 userController.js 의 postChangePassword

    ```jsx
    export const postChangePassword = async (req, res) => {
      const {
        body: { oldPassword, newPassword, newPassword1 },
      } = req;
      try {
        if (newPassword !== newPassword1) {
          // 비밀번호 확인 절차 실패
          res.status(400); // 브라우저가 비밀번호 바뀌었고 업데이트하라는 팝업이 뜨지 않도록
          res.redirect(`/users/${routes.changePassword}`);
          return;
        }
        // req.user에 changePassword() 함수가 없음!
        // await req.user.changePassword(oldPassword, newPassword);

        // DB로부터 다시 User를 불러와 changePassword가 동작할 수 있도록 한다.
        const user = await User.findById(req.user._id);
        await user.changePassword(oldPassword, newPassword);

        res.redirect(routes.me);
      } catch (error) {
        console.log(error);
        res.status(400);
        res.redirect(`/users/${routes.changePassword}`);
      }
    };
    ```

### #7.3 Adding Creator to Video

---

- 사용자가 로그인 되었을 때 비디오를 업로드할 수 있도록 하기 → 비디오에 업로드한 사용자 정보를 등록하기

> 깨달음! 현재 나의 터미널에 매순간 출력되고 있는 정보는 최초 로그인 시 입력된 req.user 정보이다. 그래서 프로필 업데이트, 비디어 업로드 시 최신 정보를 터미널에서 확인할 수 없었다. 따라서 미들웨어에서 매 순간 전달되는 loggedUser 객체를 최신으로 유지하기 위해 매번 데이터가 추가될 때마다 User 객체로부터 특정 id에 대한 User를 불러온 다음 그 내용을 req.user에 업데이트 하면 된다.

- [mongoose 함수 populate()](https://mongoosejs.com/docs/populate.html)

### #7.4 Protecting Video Routes

---

- 다른 사용자가 권한을 넘어서 url을 직접 작성해 침입하는 것을 방지하기

## #8 Custom Video Player

---

- HTML, CSS, Javascript 를 이용해 비디오 플레어를 만들었다.

## 챌린지 과제

---

- 실습한 것을 토대로 비디오 플레이어를 만드는 과제였다. 실습에서 더 추가된 것은 스페이스 바를 누르면 재생이 되어야 하고, 영상이 끝에 도달했을 때 다시 처음부터 재생이 되어야 했다. 그리고 가장 주의해서 해야 했던 기능은 화면에 커서를 가져다 대면 비디오 컨트롤러가 나타난 다음, 마우스를 비디오 플레이어 위에서 일정 시간 움직이지 않으면 비디오 컨트롤러가 사라지도록 구현해야 했다.

# 20-10-14 | Code Challenge | Voice Recorder

---

- 과제 조건
    - 강의에서 배운 것과 기본적으로 유사함. 다른 것은 카메라를 녹화하는 것이 아니라, 마이크 녹음하는 것이다. 그리고 녹음 진행 시간이 화면에 표시되어야 한다. 녹화 시 내부 함수에서 async/await를 사용하지 않고 코드를 작성해야 하며,  record 시 특정한 데이터 type을 지정해줘야 한다.
- 필요개념
    - [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream)

        > The `MediaStream` interface represents a stream of media content. A stream consists of several tracks such as video or audio tracks. Each track is specified as an instance of `MediaStreamTrack`. You can obtain a MediaStream object either by using the constructor or by calling `MediaDevices.getUserMedia()`

    - [MediaDevices](https://developer.mozilla.org/ko/docs/Web/API/MediaDevices) → 사용자의 기기(마이크, 카메라)에 접근할 수 있게 해주는 API
        - [MediaDevices.getUserMedia()](https://developer.mozilla.org/ko/docs/Web/API/MediaDevices/getUserMedia)
    - [HTMLMediaElement.srcObject](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/srcObject) → HTMLMediaElement에 연관된 미디어 소스 객체를 반환한다. 이 객체는 MediaStream, MediaSource, Blob, File이 될 수도 있다. → Blob은 뭐야?
    - [Blob](https://heropy.blog/2019/02/28/blob/)

        > JavaScript에서 Blob(Binary Large Object, 블랍)은 이미지, 사운드, 비디오와 같은 멀티미디어 데이터를 다룰 때 사용할 수 있습니다.
        대개 데이터의 크기(Byte) 및 MIME 타입을 알아내거나, 데이터를 송수신을 위한 작은 Blob 객체로 나누는 등의 작업에 사용합니다.

    - [MediaRecorder](https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder) interface
        - [MediaRecorder(stream[, options])](https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder/MediaRecorder) constructor
            - option에서 Record할 때의 데이터의 속성을 설정할 수 있다.
        - MediaRecorder.ondataavailable → Record가 시작하고 멈출 때, 또는 일정 시간 간격 때마다 발생하는 이벤트
    - setInterval(), clearInterval() → setInterval
    - [Promise](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [소스 코드 링크](https://codesandbox.io/s/20-10-14-youtube-clone-voice-recording-blueprint-forked-6m5fk?file=/src/index.js)


# 2020-10-16 | Code Challenge | Geolocation

---

## #10 API + AJAX

---

### 조회수 등록을 위한 Ajax 기능 추가

---

> 어떻게 웹 사이트의 특정 부분만 갱신되도록 할 것인가?

- 랜더링하지 않고, 어떤 동작을 하고, http status code로 답해주는 것을 만들어야 한다.
    - 라우트, 라우터, 컨트롤러 추가 → 즉, URL 경로로 들어간다는 것이 곧 새로운 페이지를 의미하는 것은 아니다.
    - **[URL에 대한 위키백과 설명](https://ko.wikipedia.org/wiki/URL)**
        - 네트워크 상에서 자원이 어디 있는지를 알려주기 위한 규약.
        - 컴퓨터 네트워크와 검색 메커니즘에서의 위치를 지정하는, 웹 리소스에 대한 참조.
        - 흔히 웹 사이트 주소로 알고 있지만, 뿐만 아니라 컴퓨터 네트워크 상의 자원을 모두 나타낼 수 있다.
        - 하지만, 그 주소에 접속하려면 해당 URL에 맞는 프로토콜을 알아야 하고, 그와 동일한 프로토콜로 접속해야 한다.

> 프론트엔드, 클라이언트 단에서는 어떻게 해야 할까?

- 수동으로 httprequest 다루는 방법 → fetch()
- fetch 안에 URL을 입력하면 실제 그 URL로 가서 요청하는 것과 똑같음.
- axios 라이브러리 다운로드

    > 좀 더 fancy한 fetch 기능 제공

    - status code

    ```jsx
    // assets/js/addComment.js

    import axios from "axios";

    // ...

    const sendComment = async (comment) => {
      const videoId = window.location.href.split("/videos/")[1];
      const response = await axios({
        url: `/api/${videoId}/comment`,
        method: "POST",
        data: {
          comment,
        },
      });
    	console.log(response);
      /* 아래와 같이 출력된다.
      ...
      ...
      config:
        adapter: ƒ xhrAdapter(config)
        data: "{"comment":"asdasd"}"
      ...
      ...
      */
      if (response.status === 200) {
        addComment(comment);
      }
    };

    // ...
    ```

    ```jsx
    // console.log(response); 결과

    {data: "", status: 200, statusText: "OK", headers: {…}, config: {…}, …}
    config:
    adapter: ƒ xhrAdapter(config)
    data: "{"comment":"asdasd"}"
    headers: {Accept: "application/json, text/plain, */*", Content-Type: "application/json;charset=utf-8"}
    maxBodyLength: -1
    maxContentLength: -1
    method: "post"
    timeout: 0
    transformRequest: [ƒ]
    transformResponse: [ƒ]
    url: "/api/5f85d70006299339881a92a9/comment"
    validateStatus: ƒ validateStatus(status)
    xsrfCookieName: "XSRF-TOKEN"
    xsrfHeaderName: "X-XSRF-TOKEN"
    __proto__: Object
    data: ""
    headers: {connection: "keep-alive", content-length: "0", date: "Fri, 16 Oct 2020 20:02:32 GMT", expect-ct: "max-age=0", referrer-policy: "no-referrer", …}
    request: XMLHttpRequest {readyState: 4, timeout: 0, withCredentials: false, upload: XMLHttpRequestUpload, onreadystatechange: ƒ, …}
    status: 200
    statusText: "OK"
    __proto__: Object
    ```

> 데이터베이스를 바꾸려면 POST, 바꾸지 않아도 된다면 GET 방식으로 URL를 얻는다.

### 댓글 기능 만들기

---

- 댓글 등록을 위한 라우트, 라우터를 만든다.
- 경로로 POST 방식으로 요청이 들어올 때 실행할 컨트롤러를 만든다.

    ```jsx
    // Add Comment 댓글 등록

    export const postAddComment = async (req, res) => {
      const {
        params: { id },
        body: { comment },
        user,
      } = req;

      try {
        const video = await Video.findById(id);
        const newComment = await Comment.create({
          text: comment,
          creator: user.id,
        });
        video.comments.push(newComment.id); // 댓글의 id를 푸시. 나중에 populate로 id를 오브젝트로 확장시킨다.
        video.save();
      } catch (error) {
        console.log(error);
        res.status(400);
      } finally {
        res.end();
      }
    };
    ```

- request의 user 정보,  body 에 들어 있는 comment 내용, 파라미터로 받아온 id 로 해당 video를 찾아 comment 리스트에 코멘트의 id를 push 해준다. 마지막으로 과정에서 오류가 일어난다면 400, 성공한다면 res.end()해줘서 응답을 끝낸다. 즉, 새로운 화면을 render 하지 않는다.

> 실제 프론트 화면에서도 실시간으로 변화를 보여줘야 한다. 그 방법은 자바스크립트!

- 댓글이 submit 되면 comment를 api URL로 post 방식으로 보내고 그 response가 200으로 성공이라면, addComment() 함수를 실행한다. 이 함수에서는 실제 화면에서 보여질 댓글을 html으로 만들어 출력한다.

```jsx
const increaseNumber = () => {
  commentNumber.innerHTML = parseInt(commentNumber.innerHTML, 10) + 1;
};

const addComment = (comment) => {
  const li = document.createElement("li");
  const span = document.createElement("span");
  span.innerHTML = comment;
  li.appendChild(span);
  commentList.prepend(li); // 가장 최신 것이 위로 오도록 추가
  increaseNumber();
};

const sendComment = async (comment) => {
	
	// ...
	
  if (response.status === 200) {
    addComment(comment);
  }
};

const handleSubmit = (event) => {
  event.preventDefault();
  const commentInput = addCommentFrom.querySelector("input");
  const comment = commentInput.value;
  sendComment(comment);
  commentInput.value = "";
};

function init() {
  addCommentFrom.addEventListener("submit", handleSubmit);
}
```

### 과제 후기

---

- 과제 내용
    - 현재 ip에 대한 주소 정보가 주어지는 특정 API URL를 FETCH 하여 받아온 JSON을 가공하여 화면에 출력하면 되는 간단한 문제였다.
- 후기
    - 웹의 세계는 무궁무진하고 그 방식도 참신하다. URL를 막연히 웹페이지 주소 정보로만 알고 있다가, 오늘 새삼스레 모든 웹 자원의 주소라는 것을 깨달았다. 멋지고 두근거린다! 앞으로 할 것들도 너무 기대된다. 새로운 배움에 세상을 좀 더 이해하고 나 스스로 성장할 수 있다고 생각하니 눈물이 날 것만 같다. 가끔 욕 나올 만큼 힘들지만, 난 이 일이 참 좋다.