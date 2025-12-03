document.addEventListener('DOMContentLoaded', function() {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const darkModeStylesheet = document.getElementById('dark-mode');
    
    // Check for saved user preference
    if (localStorage.getItem('darkMode') === 'enabled') {
        enableDarkMode();
    }
    
    // Toggle dark mode
    darkModeToggle.addEventListener('click', function() {
        if (document.body.classList.contains('dark-mode')) {
            disableDarkMode();
        } else {
            enableDarkMode();
        }
    });
    
    function enableDarkMode() {
        document.body.classList.add('dark-mode');
        darkModeStylesheet.disabled = false;
        localStorage.setItem('darkMode', 'enabled');
        darkModeToggle.textContent = 'الوضع النهاري';
    }
    
    function disableDarkMode() {
        document.body.classList.remove('dark-mode');
        darkModeStylesheet.disabled = true;
        localStorage.setItem('darkMode', 'disabled');
        darkModeToggle.textContent = 'الوضع الليلي';
    }
});