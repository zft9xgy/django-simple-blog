document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.querySelector('.dark-mode');
    const darkModeLinkId = 'dark-mode-css';


    darkModeToggle.addEventListener('click', () => {
        let darkModeLink = document.getElementById(darkModeLinkId);

        window.localStorage.setItem('theme', 'light');
        if (darkModeLink) {
            // Si el enlace ya existe, eliminarlo
            darkModeLink.parentNode.removeChild(darkModeLink);
        } else {
            // Si el enlace no existe, añadirlo
            darkModeLink = document.createElement('link');
            darkModeLink.id = darkModeLinkId;
            darkModeLink.rel = 'stylesheet';
            darkModeLink.href = './static/styles/dark.css';
            document.head.appendChild(darkModeLink);
            window.localStorage.setItem('theme', 'dark');
        }
    });

    
});