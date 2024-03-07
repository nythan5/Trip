const toggleSidebar = () => {
    var sidebar = document.getElementById("sidebar");
    var mainContent = document.getElementById("mainContent");
    
    sidebar.classList.toggle("active");
    mainContent.classList.toggle("active");
}


// remove_messages.js
document.addEventListener('DOMContentLoaded', function() {
    // Adiciona um temporizador para remover as mensagens após 5 segundos
    setTimeout(function() {
      var messages = document.querySelector('.messages');
      if (messages) {
        messages.parentNode.removeChild(messages);
      }
    }, 5000);  // 5000 milissegundos = 5 segundos
  });
  
