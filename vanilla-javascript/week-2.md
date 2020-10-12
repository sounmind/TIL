# TIL

---

## [노마드코더 | 바닐라JS 2주 완성반](https://nomadcoders.co/c/vanillajs-challenge/lobby)

---

[2주 과정 진도표](https://nomadcoders.co/faq/schedule-vanillajs) | 2020-10-05 ~ 2020-10-18

# 20-10-12 | Code Challenge | Events, localStorage

---

### 과제 목표

---

- To Do 리스트 만들기
    1. 입력
    2. 브라우저의 지역 저장소에 내용이 저장되어야 함. → 새로고침했을 때 데이터를 그대로 불러올 수 있어야 함.
    3. 리스트를 Pending, Finished 두 하위 리스트로 나눠, 버튼을 눌렀을 때 자유롭게 리스트 간 이동과 삭제를 할 수 있어야 함.

### 첫째 날

---

- 소스 코드

    ```html
    <!DOCTYPE html>
    <html>
      <head>
        <title>Parcel Sandbox</title>
        <meta charset="utf-8" />
      </head>
      <body>
        <form action="" class="toDo-form">
          <input type="text" class="toDo-input" placeholder="Add task" />
        </form>
        <h1>Pending</h1>
        <ul class="list-pending">
          <li></li>
        </ul>
        <h1>Finished</h1>
        <ul class="list-finished">
          <li></li>
        </ul>
        <script src="src/index.js"></script>
      </body>
    </html>
    ```

    ```jsx
    // index.js
    const toDoForm = document.querySelector(".toDo-form"),
      toDoInput = toDoForm.querySelector("input"),
      htmlPendingList = document.querySelector(".list-pending"),
      htmlFinishedList = document.querySelector(".list-finished");

    const PENDING_LS = "PENDING";
    const FINISHED_LS = "FINISHED";
    let pendingList = [];
    let finishedList = [];

    function loadPendingAndFinished() {
      const pendingStored = localStorage.getItem(PENDING_LS);
      const finishedStored = localStorage.getItem(FINISHED_LS);
      if (pendingStored !== null && finishedStored !== null) {
        const parsedPending = JSON.parse(pendingStored);
        const parsedFinished = JSON.parse(finishedStored);
        parsedPending.forEach(function (oneToDo) {
          addPending(oneToDo.text, oneToDo.id);
        });
        // 추가하기: 완료 목록 불러오기
      }
    }
    function handleSubmit(event) {
      event.preventDefault();
      const currentValue = toDoInput.value;
      addPending(currentValue, "new");
    }
    function addPending(text, id) {
      // id를 유지시키기: 새로운 등록이면 id 생성, 기존의 것을 불러들이면 id 그대로 가져오기
      let toDoId;
      if (id === "new") {
        toDoId = Math.floor(Math.random() * 10000000000);
      } else {
        toDoId = id;
      }
      const onePendingList = document.createElement("li");
      const deleteButton = document.createElement("button");
      deleteButton.innerHTML = "❌";
      deleteButton.addEventListener("click", deleteToDo);
      const finishButton = document.createElement("button");
      finishButton.innerHTML = "✅";
      const span = document.createElement("span");
      span.innerHTML = text;
      onePendingList.appendChild(span);
      onePendingList.appendChild(finishButton);
      onePendingList.appendChild(deleteButton);
      onePendingList.id = toDoId;
      htmlPendingList.appendChild(onePendingList);
      const toDoObj = {
        text: text,
        id: toDoId
      };
      pendingList.push(toDoObj);
      saveToDos();
    }

    function addFinished(text) {
    	// 추가하기: 완료 목록에 요소 추가하는 기능
    }

    function saveToDos() {
      localStorage.setItem(PENDING_LS, JSON.stringify(pendingList));
      localStorage.setItem(FINISHED_LS, JSON.stringify(finishedList));
    }

    function deleteToDo(event) {
      const listSelected = event.target.parentNode;
      const parentList = listSelected.parentNode;
      parentList.removeChild(listSelected);
      const filteredPending = pendingList.filter(function (toDo) {
        return toDo.id !== parseInt(listSelected.id, 10);
      });
      const filteredFinished = finishedList.filter(function (toDo) {
        return toDo.id !== parseInt(listSelected.id, 10);
      });
      pendingList = filteredPending;
      finishedList = filteredFinished;
      saveToDos();
    }

    function init() {
      loadPendingAndFinished();
      toDoForm.addEventListener("submit", handleSubmit);
    }

    init();
    ```

### 필요개념

---

- JSON.stringify()
- Math
    - Math.floor()
    - Math.random()
- list
    - push
    - filter()
    - forEach()
- event
    - target
- DOM
    - parentNode
    - createElement()
    - appendChild()
    - innerHTML
    - innerText
    - removeChild()
- parseInt(string, radix)