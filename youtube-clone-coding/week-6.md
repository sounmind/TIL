# [노마드코더 | 유튜브 클론 코딩 챌린지](https://nomadcoders.co/c/wetube-challenge/lobby)

[6주 과정 진도표](https://nomadcoders.co/faq/schedule-youtube) | 2020-9-14 ~ 2020-10-23

---

# TIL | 챌린지를 진행하며 내가 한 것과 배운 것 | 6주차

# 20-10-19 | Code Challenge

---

- 중간고사 시험 공부 때문에 하지 않았다.    



# 20-10-20 | Code Challenge | 마지막 과제

---

## 1. 댓글 삭제 기능 구현하기 (#10.5)

1. 로그인 한 상태에서, 해당 댓글이 로그인 한 유저의 댓글이면 댓글 옆에 ❌ 표시를 보이게 하기
    1. videoDeatil.pug 에서 로그인된 유저와 댓글 작성자를 확인하는 코드 작성하기.
    2. 로그인된 유저와 댓글 작성자가 일치하면 댓글 부분에 ❌ 추가하기
2.  ❌를 누르면 비동기로 댓글이 삭제되어야 한다.
    1. 삭제 버튼을 클릭하면 API 라우터를 통해 API 라우트 경로로 이동해야 한다.
        - `assets/js/comment.js` 에 함수를 추가한다.
            1. ❌에 이벤트리스너를 부착한다.
            2. handleDelete 함수를 작성한다.
            3. deleteComment 함수를 작성한다.
                - 해당 Comment Element를 삭제한다.
                - api 를 이용해  라우터→라우트→컨트롤러 순으로 POST 방식으로 요청하여 데이터베이스에 접근한다.
            4. decreaseNumber 함수를 작성하여 댓글 개수가 하나 줄어들도록 한다.
3. routes.js 에 댓글 삭제를 위한 라우트 추가
4. routes/apiRouter.js 에 삭제를 위한 라우트를 받아 post 방식으로 댓글을 삭제할 컨트롤러 함수를 호출하는 post 함수 작성
5. controllers/videoController.js 에 postDeleteComment 함수 작성

## 2. DB, Mongo Atlas에 배포 (#11.3 ~ #11.4)

## 3. 서버, Heroku에 배포 (#11.6 ~ #11.7)