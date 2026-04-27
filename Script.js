const addBtn = document.querySelector("#addBabyLionBtn");
const form = document.querySelector("#babyLionForm");
const cancelBtn = document.querySelector("#cancelBtn");

const cardArea = document.querySelector("#cardArea");
const detailArea = document.querySelector("#detailArea");

let babyLions = JSON.parse(localStorage.getItem("babyLions")) || [];

// 폼 열기
addBtn.addEventListener("click", function () {
  form.classList.remove("hidden");
});

// 폼 닫기
cancelBtn.addEventListener("click", function () {
  form.classList.add("hidden");
});

// 추가하기
form.addEventListener("submit", function (e) {
  e.preventDefault();

  const newLion = {
    name: document.querySelector("#name").value,
    track: document.querySelector("#track").value,
    skills: document.querySelector("#skills").value,
    intro: document.querySelector("#intro").value,
  };

  babyLions.push(newLion);

  localStorage.setItem("babyLions", JSON.stringify(babyLions));

  renderBabyLions();

  form.reset();
  form.classList.add("hidden");
});

// 화면에 다시 그리기
function renderBabyLions() {
  cardArea.innerHTML = "";
  detailArea.innerHTML = "";

  babyLions.forEach(function (lion) {
    cardArea.innerHTML += `
      <div class="summary-card">
        <h3>${lion.name}</h3>
        <p class="track">${lion.track}</p>
        <p>${lion.intro}</p>
      </div>
    `;

    detailArea.innerHTML += `
      <section class="detail-card">
        <h2>${lion.name}</h2>
        <p>${lion.track}</p>

        <h4>자기소개</h4>
        <p>${lion.intro}</p>

        <h4>관심 기술</h4>
        <ul>
          <li>${lion.skills}</li>
        </ul>
      </section>
    `;
  });
}

// 페이지 열릴 때 저장된 데이터 보여주기
renderBabyLions();