# TIL

---

## [노마드코더 | 바닐라JS 2주 완성반](https://nomadcoders.co/c/vanillajs-challenge/lobby)

---

[2주 과정 진도표](https://nomadcoders.co/faq/schedule-vanillajs) | 2020-10-05 ~ 2020-10-18

# 20-10-05 | 1.1 ~ 1.5 | Quiz

---

1. 프론트엔드에서 사용할 수 있는 단 하나의 프로그래밍 언어는 자바스크립트이다.
2. `ECMAScript`는 NetScape가 인터넷 상의 다양한 스크립트 언어를 하나로 묶기 위해 제시한 표준안이다.
   - 적용되는 스크립트 언어 → IE의 JScript, Adobe의 Flash ActionScript
3. 바닐라 자바스크립트는 프레임워크 또는 라이브러리 없는 순수한 자바스크립트를 뜻한다.
4. Html에서 스크립트 태그는 body 태그 아래 있어야 한다.
   1. 자바스크립트는 HTML과 CSS가 결합되고 웹페이지 상에서 올려진 후, 브라우저의 자바스크립트 엔진에 의해 실행됩니다. 이는 페이지의 구조와 스타일등을 정해놓고, 자바스크립트가 실행된다는 것과 같은 의미입니다.
   2. 동적으로 사용자 인터페이스를 업데이트하는 자바스크립트의 사용은 Document Object Model API를 통해 HTML과 CSS를 수정하는 것으로 좋은 현상입니다. 만약 자바 스크립트가 HTML과 CSS 전에 실행되었다면 문제가 분명 발생할 것입니다.
5. 자바스크립트는 해석형 언어이다.
   - 따라서 코드가 위에서 아래로 순차적으로 실행되고 그 즉시 결과가 반환된다. 브라우저에서 동작하기 전에 다른 방식으로 코드를 변환할 필요가 없다. 반면에 컴파일러형 언어는 컴퓨터에 의해 동작되기전 다른 형식으로 변환하는 언어이다. 예를 들면 C/C++과 같은 언어는 어셈블리어로 컴파일되어 동작된다.
6. 서버측 JS와 클라이언트측 JS
   - 클라이언트측 코드란, 사용자의 컴퓨터에서 작동되는 코드이다. 만약 웹페이지를 보고자 한다면, 클라이언트 측 코드가 사용자의 컴퓨터로 다운로드되고 브라우저가 이를 표시한다. 이러한 자바스크립트 모듈을 저오학히 클라이언트측 자바스크립트라고 한다.
   - 반면 서버측 코드는 서버에서 작동되고, 그 결과가 사용자의 브라우저에 넘어가 표시된다. PHP, Python, Ruby, ASP.NET등이 서버측 웹 언어의 대표적 예라고 볼 수 있습니다. 물론 자바스크립트도 가능하다. 유명한 Node.js란 환경을 통해 서버측에서도 자바스크립트가 사용 가능하다.
7. 자바스크립트의 스크립트 로딩 방법

   - 작성된 스크립트를 브라우저가 적절한 때에 로딩하는것에 대해 몇가지 이슈가 있다. 중요한 것은 모든 HTML 요소는 순서대로 페이지에 로드된다는 것이다. 만약 당신이 자바스크립트를 이용해 HTML 요소를 조작할 경우(정확하게는 DOM), 자바스크립트 코드가 조작 대상인 HTML 요소보다 먼저 실행된다면 조작할 요소가 존재하지 않는 상태이기 때문에 제대로 동작하지 않을 것이다.
   - 해결방법 1 - 내부 자바스크립트

     ```jsx
     document.addEventListener("DOMContentLoaded", function() {
       ...
     });
     ```

     이 이벤트리스너는 "DOMContentLoad" 이벤트가 발생되었을 때 function()을 실행한다는 의미이다. "DOMContentLoad" 이벤트는 브라우저가 완전히 로드되고 해석될때 발생된다. function(){} 내부의 자바스크립트 구문은 이벤트가 발생되기 전까지는 실행되지 않는다. 따라서 모든 body태그의 요소가 로드된 이후 자바스크립트 코드가 실행되도록 만들어 에러를 피할 수 있다.

   - 해결방법 2 - 외부 자바스크립트

     - 외부 자바스크립트 예제에서는 좀더 최신의 자바스크립트 문법인 async 속성을 사용하게 된다. 일반적으로 HTML요소를 로딩하는 중 `<scirpt>`태그를 만나면 JavaScript의 내용이 모두 다운될 때까지 HTML로딩은 멈추게 되는데, async요소는 비동기방식으로 `<script>`태그에 도달했을 때 브라우저에게 HTML 요소를 멈추지 않고 다운받도록 유지시킨다. ( 비동기 방식을 이해하려면 이 **[영상](https://www.youtube.com/watch?v=8aGhZQkoFbQ)**을 보면 된다! )

     ```jsx
     <script src="script.js" async></script>
     ```

     - **Note**: 외부 스크립트 경우 async 속성을 사용하면 되기 때문에 내부 스크립트처럼 DOMContentLoaded이벤트를 사용할 필요가 없다. 하지만 async속성은 외부 스크립트의 경우만 동작한다.
     - 예전 방식은 `scirpt` 요소를 `body`태그의 맨 끝에 넣는 방법이었다(`</body>` 바로 위에). 이 방식을 사용해도 `body`태그가 모두 로드된 이후 `scirpt`가 실행되게 만들 수 있다. 문제는 이 방법과 `DOMContentLoaded`를 이용한 방법 모두 `HTML DOM`이 로드되기 전까지 `script`의 로딩과 파싱이 완전히 차단된다는 문제가 있다. 이는 많은 자바스크립트 코드를 다루는 규모가 큰 사이트의 경우 사이트를 느리게 만드는 중요한 성능 문제를 야기할 수 있다. 이것이 `async` 속성을 사용해야 하는 이유이다!
     - async & defer
       - 더 깊게 들어가보면 이러한 코드문제를 해결하기 위한 방법은 실제로 두가지가 있다. — `async` 와`defer` 입니다. 두 가지의 차이를 보자.
       - async 스크립트는 페이지 렌더링의 중단 없이 스크립트를 다운로드 하고, 또한 스크립트의 다운로드가 끝나자 마자 이를 실행시킨다. async는 외부 스크립트끼리의 구체적인 실행 순서는 보장하지 않고, 단지 나머지 페이지가 나타나는 동안 스크립트가 비동기방식으로 다운로드 되어 중단되지 않는다는 것만 보장한다. async는 각각의 스크립트가 독립적으로, 서로에게 의존하지 않는 관계일 때 적절하다.
       - 만약 scirpt들이 각각의 스크립트에 의존하지 않고 독립적으로 파싱되도 상관없다면, `async` 를 사용한다.
       - 먄약 sciprt들이 의존하고 하나의 스크립트가 파싱될때까지 기다려야 한다면, `defer` 를 사용하고 각각의 `<script>` 태그들을 실행되길 원하는 순서대로 작성한다.

# 20-10-06 | 1.6 ~ 1.10 | Quiz

---

## [let](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let), [const](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const), [var](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/var) 에 대해 알기

---

[https://developer.mozilla.org/](https://developer.mozilla.org/) 에서 그대로 옮긴 것이다.

### let

---

- `let`은 변수가 선언된 블록, 구문 또는 표현식 내에서만 유효한 변수를 선언한다. 이는 `var` 키워드가 블록 범위를 무시하고 전역 변수나 함수 지역 변수로 선언되는 것과 다른 점이다.
- stackoverflow | [왜 let 을 사용해야 하는가?](https://stackoverflow.com/questions/37916940/why-was-the-name-let-chosen-for-block-scoped-variable-declarations-in-javascri)
- **유효 범위 규칙**

  - let 으로 선언된 변수는 변수가 선언된 블록 내에서만 유효하며, 당연하지만 하위 블록에서도 유효하다. 이러한 점에서는 let 과 var는 유사하지만, var는 함수 블록 이외의 블록은 무시하고 선언된다는 점이 다르다.

    ```jsx
    function varTest() {
      var x = 1;
      if (true) {
        var x = 2; // 상위 블록과 같은 변수!
        console.log(x); // 2
      }
      console.log(x); // 2
    }

    function letTest() {
      let x = 1;
      if (true) {
        let x = 2; // 상위 블록과 다른 변수
        console.log(x); // 2
      }
      console.log(x); // 1
    }
    ```

- **비공개 변수 모사**

  - [생성자](https://developer.mozilla.org/en-US/docs/Glossary/Constructor)와 함께 사용하여 [클로저](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)를 사용하지 않고 비공개 변수를 만들고 접근할 수 있다.

    ```jsx
    var Thing;

    {
      let privateScope = new WeakMap();
      let counter = 0;

      Thing = function () {
        this.someProperty = "foo";

        privateScope.set(this, {
          hidden: ++counter,
        });
      };

      Thing.prototype.showPublic = function () {
        return this.someProperty;
      };

      Thing.prototype.showPrivate = function () {
        return privateScope.get(this).hidden;
      };
    }

    console.log(typeof privateScope);
    // "undefined"

    var thing = new Thing();

    console.log(thing);
    // Thing {someProperty: "foo"}

    thing.showPublic();
    // "foo"

    thing.showPrivate();
    // 1
    ```

  - 임시적인 사각 지역과 오류

    ```jsx
    if (x) {
      let foo;
      let foo; // SyntaxError thrown.
    }
    ```

    - ECMAScript 2015에서는let은 선언 끌어올리기의 적용을 받지 않습니다. 이는 let 선언이 현재 실행되는 구간의 최상위로 옮겨지지 않는다는 것을 의미합니다. 따라서 변수가 초기화(선언)되기 전에 참조할 경우 ReferenceError가 발생합니다.(var로 선언된 변수는 undefined 값을 가지는 것과는 대조적입니다.) "임시적인 사각 지역"은 블록 시작 부분부터 변수 선언이 실행되기 전까지 입니다.
    - (let들의 정의가 평가되기까지 초기화가 되지 않는다는 의미이지. 호이스팅이 되지않아 정의가 되지 않는다는 의미와는 다르다고 생각함\_헷갈리면 안된다.)

      ```jsx
      function do_something() {
        console.log(bar); // undefined
        console.log(foo); // ReferenceError
        var bar = 1;
        let foo = 2;
      }
      ```

### const

---

- 이 선언은 선언된 함수에 전역 또는 지역일 수 있는 상수를 만듭니다. 상수 초기자(initializer)가 필요합니다. 즉 선언되는 같은 문에 그 값을 지정해야 합니다(이는 나중에 변경될 수 없는 점을 감안하면 말이 됩니다).
- 상수는 `[let](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let)` 문을 사용하여 정의된 변수와 마찬가지로 블록 범위(block-scope)입니다. 상수의 값은 재할당을 통해 바뀔 수 없고 재선언될 수 없습니다.
- `[let](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let)`에 적용한 "[일시적 사각 지대](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let#Temporal_dead_zone_and_errors_with_let)"에 관한 모든 고려는, `const`에도 적용합니다.
- 상수는 같은 범위의 상수 또는 변수와 그 이름을 공유할 수 없습니다.

### var

---

- 어디에 선언이 되어있든 간에 변수들은 어떠한 코드가 실행되기 전에 처리가 됩니다. var로 선언된 변수의 범위는 현재 실행 문맥인데, 그 문맥은 둘러싼 함수, 혹은 함수의 외부에 전역으로 선언된 변수도 될 수 있습니다.
- 선언된 변수들의 값 할당은 할당이 실행될 때 전역변수(이것은 전역 오브젝트의 프로퍼티가 됩니다)처럼 생성이 됩니다. 선언된 변수들과 선언되지 않은 변수들의 차이점은 다음과 같습니다:

  1. 선언된 변수들은 변수가 선언된 실행 콘텍스트(execution context) 안에서 만들어집니다. 선언되지 않은 변수들은 항상 전역변수 입니다.

     ```jsx
     function x() {
       y = 1; // strict 모드에서는 ReferenceError를 출력합니다.
       var z = 2;
     }

     x();

     console.log(y); // 로그에 "1" 출력합니다.
     console.log(z); // ReferenceError: z is not defined outside x를 출력합니다.
     ```

  2. 선언된 변수들은 어떠한 코드가 실행되기 전에 만들어집니다. 선언되지 않은 변수들은 변수들을 할당하는 코드가 실행되기 전까지는 존재하지 않습니다.

     ```jsx
     console.log(a); // ReferenceError를 출력합니다.
     console.log("still going..."); // 결코 실행되지 않습니다.
     ```

     ```jsx
     var a;
     console.log(a); // 브라우저에 따라 로그에 "undefined" 또는 "" 출력합니다.
     console.log("still going..."); // 로그에 "still going..." 출력합니다.
     ```

  3. 선언된 변수들은 변수들의 실행 콘텍스트(execution context)의 프로퍼티를 변경되지 않습니다. 선언되지 않은 변수들은 변경 가능합니다. (e.g 삭제 될 수도 있습니다.)

     ```jsx
     var a = 1;
     b = 2;

     delete this.a; // strict 모드에서는 TypeError를 출력합니다. 그렇지 않으면 자동적으로 실패합니다.
     delete this.b;

     console.log(a, b); // ReferenceError를 출력합니다.
     // 'b' 프로퍼티는 삭제되었고, 어디에도 존재하지 않습니다.
     ```

  - 이러한 세가지 다른 점 때문에, 변수 선언 오류는 예기치 않은 결과로 이어질 가능성이 높습니다. 그러므로 함수 또는 전역 범위인지 여부와 상관없이, 항상 변수를 선언 하는 것을 추천합니다. 그리고 ECMAScript 5 안에 strict mode, 선언되지 않은 변수에 할당하면 오류를 출력합니다.

- var 호이스팅(hoisting)

  - 변수 선언들 (그리고 일반적인 선언)은 어느 코드가 실행 되기 전에 처리하기 때문에, 코드 안에서 어디서든 변수 선언은 최상위에 선언한 것과 동등합니다. 이것은 변수가 선언되기 전에 사용 될 수 있다는 것을 의미합니다. 변수 선언이 함수 또는 전역 코드의 상단에 이동하는 것과 같은 행동을 "호이스팅(hoisting)"이라고 불립니다.

    ```jsx
    bla = 2;
    var bla;
    // ...

    // 위 선언을 다음과 같이 암묵적으로 이해하면 됩니다:

    var bla;
    bla = 2;
    ```

  - 이러한 이유로, 그들의 범위(전역 코드의 상단 그리고 함수 코드의 상단) 상단에 변수를 항상 선언하기를 권장합니다. 그러면 변수는 함수 범위 (지역)이 되며, 스코프 체인으로 해결될 것이 분명합니다.

# 20-10-07 | Code Challenge | Objects, Arrays and Events

---

- [이벤트 참조](https://developer.mozilla.org/ko/docs/Web/Events)
  - 마우스 이벤트 enter, over의 차이점은?
    - enter는 진입했을 때 한 번만 발생한다.
    - over는 진입하고 나서도 계속 발생한다.

### 챌린지를 통해 배운 것: 선언 순서... 미친...

---

- 계속 이게 왜 안 되지? 의문이었는데 선언 순서 때문이었다. 그리고 함수 이름과 함수 이름에 괄호를 달아줄 때 차이 또한 잘 알아야 한다.

```jsx
const greeting = document.querySelector(".greeting");

function handleResize() {
  console.log("resized");
  greeting.innerHTML = "It has been resized!";
  greeting.style.color = `${colors[1]}`;
}

function handleMouseEnter() {
  console.log("Mouse Enter");
  greeting.innerHTML = "Mouse is inside of me!";
  greeting.style.color = `${colors[2]}`;
}

function handleMouseOut() {
  console.log("Mouse Out");
  greeting.innerHTML = "Mouse is gone!";
  greeting.style.color = `${colors[3]}`;
}

function handleClickRight() {
  console.log("Right Click");
  greeting.innerHTML = "Right Clicked!";
  greeting.style.color = `${colors[4]}`;
}

const superEventHandler = {
  resize: handleResize,
  mouseEnter: handleMouseEnter,
  mouseOut: handleMouseOut,
  clickRight: handleClickRight,
};

window.addEventListener("resize", superEventHandler.resize);
greeting.addEventListener("mouseenter", superEventHandler.mouseEnter);
greeting.addEventListener("mouseout", superEventHandler.mouseOut);
window.addEventListener("contextmenu", superEventHandler.clickRight);
```

# 20-10-08 | Code Challenge | if, else, events

---

- 윈도우를 횡방향으로 드래그하여 크기를 변화시켰을 때, 특정 크기 범위에 따라 body의 배경색이 달라지면 된다.
- 사용 개념
  - [`window.onresize`](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onresize) → 윈도우의 사이즈가 변할 때마다 호출된다. `addEventListener('resize', 함수이름)`와 같은 기능이다.
  - [`Window.innerWidth`](https://developer.mozilla.org/en-US/docs/Web/API/Window/innerWidth) → 윈도우 안의 내부 너비를 반환한다. 스크롤바의 너비까지 포함한다. 더 정확히, 윈도우의 레이아웃 뷰포트의 너비를 반환하는데, **[레이아웃 뷰포트](https://developer.mozilla.org/en-US/docs/Glossary/layout_viewport)**는 웹페이지를 그리는데(뿌리는데) 현재 사용자가 사용하느 기기에서 보이는 화면의 공간이다.
- 방법

  - css에 클래스에 따른 배경색을 정의해놓고, 윈도우 사이즈에 따라 클래스 이름을 추가하고 지우며 배경색을 바꿔도 된다.
  - 내가 선택한 방법은 윈도우의 사이즈가 변할 때마다 init 함수를 호출해 윈도우 너비를 구하고 너비에 따라 직접 body의 배경색을 바꿔주는 것이었다.

    ```jsx
    const body = document.querySelector("body");

    function init() {
      const windowWidth = window.innerWidth;
      console.log(windowWidth);
      if (windowWidth <= 500) {
        body.style.backgroundColor = "skyblue";
      } else if (windowWidth > 500 && windowWidth < 1000) {
        body.style.backgroundColor = "purple";
      } else {
        body.style.backgroundColor = "yellow";
      }
    }
    window.onresize = init;
    ```

- 크리스마스 이브까지 남은 시간은 (일, 시간, 분, 초) 형식으로 `setInterval()`을 활용하여 매 초 출력하는 과제였다.
- 계산 식이 복잡한 것 같은데 리팩토링이 필요할 것 같다.

```jsx
const clock = document.querySelector(".time-left");

function getTime() {
  // Don't delete this.
  const xmasDay = new Date("2020-12-24:00:00:00+0900"),
    now = new Date(),
    millisecondsLeft = xmasDay - now,
    day = Math.floor(millisecondsLeft / 1000 / 60 / 60 / 24),
    hour = Math.floor(millisecondsLeft / 1000 / 60 / 60 - day * 24),
    minute = Math.floor(
      millisecondsLeft / 1000 / 60 - (day * 24 * 60 + hour * 60)
    ),
    second = Math.floor(
      millisecondsLeft / 1000 -
        (day * 24 * 60 * 60 + hour * 60 * 60 + minute * 60)
    );

  clock.innerText = `
${day < 10 ? `0${day}` : day}d 
${hour < 10 ? `0${hour}` : hour}h 
${minute < 10 ? `0${minute}` : minute}m 
${second < 10 ? `0${second}` : second}s `;

} // getTime() end

function init() {
  getTime();
  setInterval(getTime, 1000);
}

init();
```

## 참고 자료

---

- Mozilla | [Javascript가 뭔가요?](https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
  - Javascript로 API를 사용할 수 있다.
    - API는 이미 만들어진 코드의 집합체라고 볼 수 있으며, 개발자들이 만들기 어렵고 힘든 부분을 쉽게 구현하도록 하는 프로그램이다.
    - DOM API, Geolocation API, Canvas, WebGL API, Audio and Video API
- 생활코딩 | [Javascript](https://opentutorials.org/course/743)
- 유튜브 | [What the heck is the event loop anyway?](https://www.youtube.com/watch?v=8aGhZQkoFbQ)
- 유튜브 | [자바스크립트의 역사와 현재 그리고 미래 (JavaScript, ECMAScript, JQuery, Babel, Node.js)](https://www.youtube.com/watch?v=wcsVjmHrUQg)
