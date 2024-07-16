const toggle = document.querySelector('.dark-mode');

toggle.addEventListener('click', function() {
  const isCurrentlyDarkMode = document.documentElement.classList.contains('dark');

  if (isCurrentlyDarkMode) {
    document.documentElement.classList.remove('dark');
    document.documentElement.classList.add('light');
    localStorage.setItem('theme', 'light');
  } else {
    document.documentElement.classList.add('dark');
    document.documentElement.classList.remove('light');
    localStorage.setItem('theme', 'dark');
  }
});

const savedTheme = localStorage.getItem('theme');

if (savedTheme === 'dark') {
  document.documentElement.classList.add('dark');
  document.documentElement.classList.remove('light');
} else if (savedTheme === 'light') {
  document.documentElement.classList.remove('dark'); 
  document.documentElement.classList.add('light');
 
}


// Check to see if Media-Queries are supported
if (window.matchMedia) {
    // Check if the dark-mode Media-Query matches
    if(window.matchMedia('(prefers-color-scheme: dark)').matches){
      // Dark
      console.log('dark')
    } else {
      // Light
      console.log('light')
    }
  } else {
    // Default (when Media-Queries are not supported)
    console.log('default')
  }