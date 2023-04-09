const loginForm = document.getElementById("loginForm");
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (username === "member1" && password === "password1") {
    location.replace("member1-dashboard.html");
  } else if (username === "member2" && password === "password2") {
    window.location.href = "member2-dashboard.html";
  } else if (username === "member3" && password === "password3") {
    window.location.href = "member3-dashboard.html";
  } else {
    alert("Invalid login credentials");
  }
});
