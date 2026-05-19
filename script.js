let score = 0;

const scoreText = document.getElementById("score");
const messageText = document.getElementById("message");
const playBtn = document.getElementById("playBtn");

// reset 버튼 생성
const resetBtn = document.createElement("button");
resetBtn.textContent = "RESET";
document.querySelector(".container").appendChild(resetBtn);

playBtn.addEventListener("click", () => {

    const randomNumber = Math.floor(Math.random() * 10) + 1;

    score += randomNumber;

    scoreText.textContent = `현재 점수: ${score}`;

    messageText.textContent = `+${randomNumber} 점 획득!`;

    if (score >= 50) {
        messageText.textContent = "🏆 승리!";
        playBtn.disabled = true;
    }
});

// reset 기능
resetBtn.addEventListener("click", () => {
    score = 0;

    scoreText.textContent = "현재 점수: 0";
    messageText.textContent = "게임이 초기화되었습니다.";

    playBtn.disabled = false;
});