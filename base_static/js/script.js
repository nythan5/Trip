const toggleSidebar = () => {
    var sidebar = document.getElementById("sidebar");
    var mainContent = document.getElementById("mainContent");
    
    sidebar.classList.toggle("active");
    mainContent.classList.toggle("active");
}