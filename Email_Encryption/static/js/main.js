// Theme
const themeToggle = document.querySelector(".checkbox");
const body = document.querySelector("body");

// dark mode will stay after refreshing the page
const darkmode = localStorage.getItem("dark");

if (darkmode) {
  body.classList.add("dark");
  themeToggle.checked = true;
}

themeToggle.addEventListener("change", function () {
  body.classList.toggle("dark");

  if (body.classList.contains("dark")) {
    // dark mode will stay after refreshing the page
    localStorage.setItem("dark", "active");
  } else {
    localStorage.removeItem("dark");
  }
});