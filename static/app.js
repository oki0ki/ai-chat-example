// Elementy DOM
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.getElementById('chatMessages');

// Obsługa naciśnięcia Enter
messageInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter' && messageInput.value.trim() !== '') {
        sendMessage();
    }
});

// Funkcja wysyłania wiadomości
async function sendMessage() {
    const message = messageInput.value.trim();
    
    if (message === '') return;
    
    // Wyczyść input
    messageInput.value = '';
    
    // Dodaj wiadomość użytkownika
    addMessage(message, 'user');
    
    // Pokaż wskaźnik pisania
    showTypingIndicator();
    
    // Wyślij wiadomość do API
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message
            })
        });
        
        if (!response.ok) {
            throw new Error('Błąd połączenia');
        }
        
        const data = await response.json();
        
        // Usuń wskaźnik pisania
        removeTypingIndicator();
        
        // Dodaj odpowiedź bota
        addMessage(data.bot_response, 'bot');
        
    } catch (error) {
        removeTypingIndicator();
        addMessage('Przepraszam, wystąpił błąd połączenia.', 'bot');
        console.error('Error:', error);
    }
}

// Dodawanie wiadomości do czatu
function addMessage(text, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}-message`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.textContent = text;
    
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    
    // Przewiń do dołu
    scrollToBottom();
}

// Pokaż wskaźnik pisania
function showTypingIndicator() {
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message';
    typingDiv.id = 'typingIndicator';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    const indicator = document.createElement('span');
    indicator.className = 'typing-indicator';
    indicator.innerHTML = '<span></span><span></span><span></span>';
    
    contentDiv.appendChild(indicator);
    typingDiv.appendChild(contentDiv);
    chatMessages.appendChild(typingDiv);
    
    scrollToBottom();
    
    // Disable send button
    sendButton.disabled = true;
}

// Usuń wskaźnik pisania
function removeTypingIndicator() {
    const typingIndicator = document.getElementById('typingIndicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
    
    // Enable send button
    sendButton.disabled = false;
    messageInput.focus();
}

// Przewijanie do dołu
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Fokus na input przy załadowaniu
window.addEventListener('load', () => {
    messageInput.focus();
});
