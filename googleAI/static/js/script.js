document.addEventListener('DOMContentLoaded', () => {
  const userInput = document.getElementById('user-input');
  const sendButton = document.getElementById('send-button');
  const chatWindow = document.querySelector('.chat-window');
  const genreElement = document.getElementById('genre');
  const lyricsElement = document.getElementById('lyrics');
  const titleElement = document.getElementById('title');

  sendButton.addEventListener('click', sendMessage);
  userInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
      sendMessage();
    }
  });

  function sendMessage() {
    const message = userInput.value.trim();
    if (message !== '') {
      appendMessage('user', message);
      userInput.value = '';

      let requestType = '';
      if (message.toLowerCase().includes('genre')) {
        requestType = 'genre';
      } else if (message.toLowerCase().includes('lyrics')) {
        requestType = 'lyrics';
      } else if (message.toLowerCase().includes('title')) {
        requestType = 'title';
      }

      fetch('/send_message', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message, requestType }),
      })
        .then((response) => response.json())
        .then((data) => {
          appendMessage('bot', data.response);
          if (data.genre) {
            genreElement.textContent = data.genre.replace('Selected genre:', '').trim();
          }
          if (data.lyrics) {
            lyricsElement.textContent = data.lyrics.replace('Generated lyrics:', '').trim();
            lyricsElement.style.whiteSpace = 'pre-wrap';
          } else {
            lyricsElement.textContent = '';
          }
          if (data.title) {
            titleElement.textContent = data.title.replace('Suggested title:', '').trim();
          } else {
            titleElement.textContent = '';
          }
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }
  }

  function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.textContent = message;
    chatWindow.appendChild(messageElement);
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }
});