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