const addBtn = document.querySelector("#addBabyLionBtn");
const form = document.querySelector("#babyLionForm");
const cancelBtn = document.querySelector("#cancelBtn");

addBtn.addEventListener("click", function () {
  form.classList.toggle("hidden");
});

cancelBtn.addEventListener("click", function () {
  form.classList.add("hidden");
});

form.addEventListener("submit", function(e) {
  e.preventDefault();
});