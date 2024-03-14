// remove_messages.js
document.addEventListener('DOMContentLoaded', function() {
    // Adiciona um temporizador para remover as mensagens após 5 segundos
    setTimeout(function() {
      let messages = document.querySelector('.messages');
      if (messages) {
        messages.parentNode.removeChild(messages);
      }
    }, 2500);  // 5000 milissegundos = 5 segundos
  });
  