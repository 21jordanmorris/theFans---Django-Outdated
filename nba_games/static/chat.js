updateScrollChatBox();
document.body.scrollTop = 0; // For Safari
document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera

const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new ReconnectingWebSocket(
    'ws://'
    + window.location.host
    + '/ws/games/'
    + roomName
    + '/'
);

//<p class="idv-message"><span class="msg-meta">{{ msg.author }}  <span class="time">  {{ msg.timestamp }}</span></span></br>{{ msg.content }}</p>

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    
    var date = new Date();
    var pMessage = document.createElement("p");
    pMessage.className = "idv-message";

    pMessage.innerHTML = '<span class="msg-meta">' + data.author + ' <span class="time">'+ date +'</span></span></br>' + data.message;

    var element = document.getElementById("messages");
    element.appendChild(pMessage);
    updateScrollChatBox();
    //element.insertBefore(pMessage, element.childNodes[0]);
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

//document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const username = document.querySelector('#user').innerHTML;
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'channel': roomName,
        'username': username,
    }));
    messageInputDom.value = '';
};

function updateScrollChatBox() {
    var element = document.querySelector('.chat-box');
    element.scrollTop = element.scrollHeight;
}