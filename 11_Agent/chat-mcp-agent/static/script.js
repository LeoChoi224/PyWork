/**
 * 🟦 자바스크립트 클라이언트 로직
 * script.js 파일은 사용자 입력을 처리하고, 서버와 통신하며,
 * 스트리밍 응답을 화면에 표시하는 클라이언트 측 로직을 담당합니다. 주요 기능은 다음과 같습니다.
 * • 고유한 세션 ID 생성 및 관리
 * • 사용자 메시지 전송 및 표시
 * • 서버의 스트리밍 응답을 실시간으로 받아 표시
 * • 마크다운 형식의 응답을 HTML로 변환하여 렌더링
 */


// 🟦 마크다운 렌더러 설정
const renderer = {
    // link(href, title, text)는 마크다운의 [text](href "title") 문법을 만났을 때 호출됩니다.
    // href: 링크 주소, title: 툴팁으로 쓰일 제목(optional), text: 화면에 표시될 링크 텍스트
    link(href, title, text){
        // marked.js 의 기본 '링크' 렌더러 호출 -> <a href="..." title="...">text</a> 형태의 HTML문자열
        const link = marked.Renderer.prototype.link.call(this, href, title, text);

        // 채팅창에 등장한 링크를 클릭해도 현재 채팅화면은 유지하고 새 탭에 링크 화면 뜨게 하기위해.
        return link.replace("<a", "<a target='_blank' rel='noreferrer'")
    },

};

// marked.use()로 위에서 정의한 renderer를 marked.js 전역 설정에 병합합니다.
// 이후 marked.parse()를 호출할 때마다 이 커스텀 link 렌더러가 자동 적용됩니다.
marked.use({
    renderer,
});

//  🟦 세션 ID 생성 함수
//  * generateSessionId() 함수는 타임스탬프와 랜덤 문자열을 조합하여
//  * 각 채팅 세션에 대한 고유ID를 생성합니다.
//  * 이 ID는 서버가 대화 기록을 관리하는 데 필수적입니다.
/**
 * 고유한 세션 ID를 생성합니다.
 * @returns {string} 생성된 세션 ID
 */
const generateSessionId = () => {
  // Date.now(): 1970-01-01 UTC 기준 현재까지 경과한 밀리초(ms)를 숫자로 반환합니다.
  // 세션이 생성된 시점을 식별하는 데 사용됩니다.
  const timestamp = Date.now();
  // Math.random(): 0 이상 1 미만의 난수를 생성합니다.
  // .toString(36): 숫자를 36진법(0-9, a-z) 문자열로 변환하여 "0.xxxxx" 형태의 결과를 얻습니다.
  // .substring(2, 9): 앞의 "0." 부분을 잘라내고, 그 뒤 7자리 정도의 랜덤 문자열만 취합니다.
  // 같은 타임스탬프에 여러 세션이 생성되더라도 충돌하지 않도록 무작위성을 더하는 역할입니다.
  const randomString = Math.random().toString(36).substring(2, 9);
  // 템플릿 리터럴로 "session_<타임스탬프>_<랜덤문자열>" 형태의 최종 ID를 조합합니다.
  // 예: "session_1735689600000_a1b2c3d"
  return `session_${timestamp}_${randomString}`;
};

// 🟦 ChatApp 모듈: 초기화 및 이벤트 처리
//    채팅 애플리케이션의 핵심로직을 담는 ChatApp 모듈 정의

/**
 * 채팅 애플리케이션을 관리하는 모듈
 * 객체 리터럴 방식의 모듈 패턴으로, class 대신 하나의 객체 안에
 * 상태(elements, sessionId)와 동작(메서드)을 함께 묶어 관리합니다.
 * 별도의 인스턴스를 생성하지 않고 ChatApp 자체를 싱글턴처럼 사용합니다.
 */
const ChatApp = {
    // DOM 요소들을 저장할 객체
    // init() 실행 전에는 모두 null이며, init() 시점에 실제 DOM 노드로 채워집니다.
    elements: {
        chatForm: null,   // 메시지 입력 폼(<form id="chat-form">)
        chatInput: null,  // 텍스트 입력창(<input id="chat-input">)
        chatBox: null,    // 대화 내용이 쌓이는 컨테이너(<div id="chat-box">)
    },

    // 세션 ID
    // 이 클라이언트(브라우저 탭)가 서버와 나누는 대화를 식별하는 고유 값입니다.
    // 서버는 이 값으로 대화 기록(히스토리)을 세션별로 구분해 관리합니다.
    sessionId: null,


    // 앱 초기화 함수
    init(){
        // DOM 요소들 찾아서 저장.
        this.elements.chatForm = document.getElementById("chat-form");
        this.elements.chatInput = document.getElementById("chat-input");
        this.elements.chatBox = document.getElementById("chat-box");

        // 세션 ID를 생성하고 로그에 기록합니다.
        // 페이지가 로드될 때마다(새로고침 포함) 새로운 세션 ID가 발급됩니다.
        this.sessionId = generateSessionId();
        console.log("새로운 세션 ID:", this.sessionId);        

        // 이벤트 리스너 등록
        this.elements.chatForm.addEventListener(
            "submit",
            this.handleFormSubmit.bind(this)
        );
    },  // end init()

    // 채팅폼 제출 이벤트 처리
    async handleFormSubmit(e){
        e.preventDefault();
        // 사용자 입력 메세지 가져오기
        const message = this.elements.chatInput.value.trim();

        // 공백만 입력했거나 빈 문자열이면 아무 것도 하지 않고 종료합니다.
        if (!message) {
            return;
        }        

        // 사용자 메세지를 화면에 출력.
        this.appendMessage("user", message);
        this.elements.chatInput.value = "";  // 기존 입력창 비우기

        // 봇의 응답을 스트리밍
        const botMessageElement = this.createMessageElement("bot");
        await this.streamBotReponse(message, botMessageElement);
    },  // end handleFormSubmit()

    // 🟦 스트리밍 응답 처리
    async streamBotReponse(message, botMessageElement){

        try {

            const response = await fetch("/chat", {
                method: "POST",
                headers: {"Content-Type": "application/x-www-form-urlencoded"},
                // URLSearchParams는 { message, session_id } 객체를
                // "message=...&session_id=..." 형태의 쿼리 문자열로 자동 인코딩해 줍니다.
                body: new URLSearchParams({
                    message: message,
                    session_id: this.sessionId,
                }),
            });

            // HTTP 응답코드 200 아니면 예외 발생!
            if(!response.ok){
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            // 확인용
            // botMessageElement.innerHTML = await response.text();

            // response.body는 ReadableStream이며, getReader()로 스트림을 청크 단위로
            // 직접 읽을 수 있는 reader 객체를 얻습니다. (서버가 SSE/청크 스트리밍으로 응답)
            const reader = response.body.getReader();

            // 서버에서 오는 데이터는 바이트(Uint8Array)이므로, 이를 문자열로 디코딩할 TextDecoder를 준비합니다.
            const decoder = new TextDecoder();

            // 스트리밍 수신하여 누적할 텍스트(마크변환) 저장 변수
            let content = "";

            // 스트림을 읽어서 화면에 점진적으로 표시합니다.
            // 무한 루프를 돌며 reader.read()로 청크를 하나씩 꺼내고,
            // 서버가 스트림을 종료하면(done === true) 반복을 빠져나갑니다.      
            while(true){
                // value: 이번에 수신한 청크(Uint8Array), done: 스트림 종료 여부
                const { value, done } = await reader.read();
                if (done) break;

                console.log(`value =`, value);

                // 이번 청크를 문자열로 디코딩하여 누적 콘텐츠에 이어 붙입니다.
                // { stream: true } 옵션은 멀티바이트 문자(예: 한글)가 청크 경계에서
                // 잘리는 경우에도 다음 청크와 합쳐 올바르게 디코딩되도록 해 줍니다.
                content += decoder.decode(value, { stream: true });

                // 누적된 전체 마크다운 텍스트를 매 청크마다 다시 HTML로 파싱하여
                // 봇 메시지 요소에 통째로 반영합니다. (부분 마크다운도 자연스럽게 갱신됨)
                botMessageElement.innerHTML = marked.parse(content);

                // 새 내용이 추가 될 때마다 채티창 맨 아래로 스크롤
                this.scrollToBottom();
            }


        } catch(error) {
            // 네트워크 오류, HTTP오류, 스트림 읽기중 에러... 여기서 처리
            console.error("스트리밍 중 오류 발생:", error);

            botMessageElement.innerHTML = 
                "😥죄송합니다. 메시지 처리중 오류가 발생했습니다";
        }

    }, // end streamBotReponse()



    // 🟦 UI 관련 메소드들
    // createMessageElement() 메서드는 새로운 메시지 div 요소를 생성하고
    // 적절한 CSS 클래스를 추가합니다. user-message와 bot-message 클래스로 구분하여 스타일링
    createMessageElement(sender){
        // 빈 <div> 요소를 새로 생성합니다. 아직 DOM에는 붙어있지 않은 상태입니다.
        const messageElement = document.createElement("div");
        // 공통 클래스 "message"와, 보낸 사람에 따라 "user-message" 또는 "bot-message"를
        // 함께 부여하여 CSS에서 발신자별로 다른 스타일(정렬, 배경색 등)을 적용할 수 있게 합니다.
        messageElement.classList.add("message", `${sender}-message`);
        // 생성한 요소를 채팅박스 컨테이너의 마지막 자식으로 추가하여 화면에 실제로 표시합니다.
        this.elements.chatBox.appendChild(messageElement);
        // 새 요소가 추가된 직후 스크롤을 맨 아래로 내려 사용자가 바로 볼 수 있게 합니다.
        this.scrollToBottom();
        // 호출한 쪽(handleFormSubmit, appendMessage 등)에서 이 요소에
        // 이후 내용을 채워 넣을 수 있도록 참조를 반환합니다.
        return messageElement;
    },

    // appendMessage() 메서드는 메시지 요소를 생성하고 마크다운을 파싱하여 내용을 추가합니다.
    // 사용자 메시지도 마크다운으로 파싱되므로 코드 블록이나 링크 등을 입력할 수 있습니다.
    appendMessage(sender, text){
        // createMessageElement()로 발신자에 맞는 빈 메시지 박스를 먼저 만듭니다.
        const messageElement = this.createMessageElement(sender);
        // text(마크다운 원문)를 marked.parse()로 HTML 문자열로 변환한 뒤
        // innerHTML에 대입하여 렌더링합니다. (사용자 입력도 동일하게 마크다운 처리됨)
        messageElement.innerHTML = marked.parse(text);        
    },

    // scrollToBottom() 메서드는 새 메시지가 추가될 때마다 채팅 박스를 가장 아래로 스크롤하여
    // 최신 메시지가 항상 보이도록 합니다.
    scrollToBottom() {
        // scrollTop을 scrollHeight(전체 콘텐츠 높이)로 설정하면
        // 스크롤이 항상 컨테이너의 맨 아래로 이동합니다.
        this.elements.chatBox.scrollTop = this.elements.chatBox.scrollHeight;
    },    

};  // end ChatApp

// DOM 이 로딩되면 애플리케이션 초기화
document.addEventListener("DOMContentLoaded", () => {
  ChatApp.init();
});

