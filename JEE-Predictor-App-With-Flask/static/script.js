
function validateForm() {
    let phone_digits = document.getElementById('phone').value;
    let marks = document.getElementById('marks').value;

    if (phone_digits.length != 10) {
        alert('Please enter a valid 10 digit phone number');
        return false;
    }
    if (marks > 300) {
        alert('Please enter a valid marks (max 300)');
        return false;
    }

    return true; 
}
// This runs on every page load
window.onload = function () {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        document.getElementById("theme-link").setAttribute("href", "/static/" + savedTheme + ".css");
        document.getElementById("theme-toggle").innerHTML = savedTheme === "dark" ? "☀️" : "🌙";
    }
};

function toggleTheme() {
    const themeLink = document.getElementById("theme-link");
    const currentTheme = themeLink.getAttribute("href");

    if (currentTheme.includes("dark.css")) {
        themeLink.setAttribute("href", "/static/light.css");
        document.getElementById("theme-toggle").innerHTML = "🌙";
        localStorage.setItem("theme", "light");
    } else {
        themeLink.setAttribute("href", "/static/dark.css");
        document.getElementById("theme-toggle").innerHTML = "☀️";
        localStorage.setItem("theme", "dark");
    }
}
