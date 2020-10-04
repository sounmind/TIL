# TIL

---

## [노마드코더 | 바닐라JS 2주 완성반](https://nomadcoders.co/c/vanillajs-challenge/lobby)

---

[6주 과정 진도표](https://nomadcoders.co/faq/schedule-vanillajs) | 2020-9-14 ~ 2020-10-23

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
        - 외부 자바스크립트 예제에서는 좀더 최신의 자바스크립트 문법인 async 속성을 사용하게 된다. 일반적으로 HTML요소를 로딩하는 중 <scirpt>태그를 만나면 JavaScript의 내용이 모두 다운될 때까지 HTML로딩은 멈추게 되는데, async요소는 비동기방식으로 <script>태그에 도달했을 때 브라우저에게 HTML 요소를 멈추지 않고 다운받도록 유지시킨다. ( 비동기 방식을 이해하려면 이 **[영상](https://www.youtube.com/watch?v=8aGhZQkoFbQ)**을 보면 된다! )

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

## 참고 자료

---

- Mozilla | [Javascript가 뭔가요?](https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
    - Javascript로 API를 사용할 수 있다.
        - API는 이미 만들어진 코드의 집합체라고 볼 수 있으며, 개발자들이 만들기 어렵고 힘든 부분을 쉽게 구현하도록 하는 프로그램이다.
        - DOM API, Geolocation API, Canvas, WebGL API, Audio and Video API
- 생활코딩 | [Javascript](https://opentutorials.org/course/743)
- 유튜브 | [What the heck is the event loop anyway?](https://www.youtube.com/watch?v=8aGhZQkoFbQ)
- 유튜브 | [자바스크립트의 역사와 현재 그리고 미래 (JavaScript, ECMAScript, JQuery, Babel, Node.js)](https://www.youtube.com/watch?v=wcsVjmHrUQg)