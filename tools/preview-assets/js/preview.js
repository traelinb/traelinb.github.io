(function () {
  var button = document.getElementById("theme-toggle");
  function updateLabel() {
    var dark = document.documentElement.dataset.theme === "dark";
    button.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
    button.setAttribute("aria-pressed", String(dark));
  }
  button.addEventListener("click", function () {
    var theme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = theme;
    try { localStorage.setItem("hang-yi-theme", theme); } catch (error) {}
    updateLabel();
  });
  updateLabel();
})();
