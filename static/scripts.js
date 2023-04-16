const chatbox = document.getElementById("chatbox");
const userInput = document.getElementById("userInput");
const thinkingIndicator = document.getElementById("thinking");

// Initialize marked.js and highlight.js
marked.setOptions({
    highlight: function(code, language) {
        if (language && hljs.getLanguage(language)) {
            return hljs.highlight(code, { language }).value;
        }
        return hljs.highlightAuto(code).value;
    },
    breaks: true,
});

userInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage(userInput.value);
        userInput.value = "";
    }
});

function autoResizeTextarea() {
    userInput.style.height = "auto";
    userInput.style.height = this.scrollHeight + "px";
}
userInput.addEventListener("input", autoResizeTextarea);

        

async function sendMessage(message) {
    const data = {user_input: message};
    const userMessageDiv = addToChatbox("User", message);
    autoResizeTextarea();
    chatbox.insertBefore(thinkingIndicator, userMessageDiv.nextSibling);
    thinkingIndicator.style.display = "flex";
    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });
    thinkingIndicator.style.display = "none";

    if (response.ok) {
        const responseData = await response.json();
        addToChatbox("Assistant", responseData.response);
    } else {
        console.error("Error sending message to server");
    }
}

function addToChatbox(role, message) {
    const emoji = role === "User" ? "👤" : "🤖";
    const messageDiv = document.createElement("div");
    messageDiv.classList.add(role.toLowerCase());
    messageDiv.innerHTML = `<span>${emoji}</span><div class="message">${marked.parse(message)}</div>`;
    chatbox.appendChild(messageDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
    return messageDiv;
}