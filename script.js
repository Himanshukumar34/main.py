const words = ["apple", "grape", "lemon", "table", "chair"];
let secretWord;
let attempts;
let guessedLetters;

const wordDisplay = document.getElementById('wordDisplay');
const attemptsSpan = document.getElementById('attempts');
const message = document.getElementById('message');
const guessInput = document.getElementById('guessInput');
const guessBtn = document.getElementById('guessBtn');
const guessedLettersDiv = document.getElementById('guessedLetters');
const restartBtn = document.getElementById('restartBtn');

function startGame() {
    secretWord = words[Math.floor(Math.random() * words.length)];
    attempts = 6;
    guessedLetters = [];
    wordDisplay.textContent = "_ ".repeat(secretWord.length);
    attemptsSpan.textContent = attempts;
    message.textContent = "";
    guessedLettersDiv.textContent = "Guessed letters: ";
    guessInput.value = "";
    guessInput.disabled = false;
    guessBtn.disabled = false;
}

function updateWordDisplay() {
    let display = "";
    for (let ch of secretWord) {
        display += guessedLetters.includes(ch) ? ch + " " : "_ ";
    }
    wordDisplay.textContent = display.trim();
}

guessBtn.addEventListener('click', () => {
    const guess = guessInput.value.toLowerCase();
    message.textContent = "";

    if (!guess || guess.length !== 1 || !/[a-z]/.test(guess)) {
        message.textContent = "❌ Please enter a valid letter";
        guessInput.value = "";
        return;
    }

    if (guessedLetters.includes(guess)) {
        message.textContent = "⚠ You already guessed this letter";
        guessInput.value = "";
        return;
    }

    guessedLetters.push(guess);

    if (secretWord.includes(guess)) {
        message.textContent = "✅ Good guess!";
    } else {
        message.textContent = "❌ Wrong guess!";
        attempts--;
        attemptsSpan.textContent = attempts;
    }

    guessedLettersDiv.textContent = "Guessed letters: " + guessedLetters.join(", ");
    updateWordDisplay();

    if (!wordDisplay.textContent.includes("_")) {
        message.textContent = "🎉 Congratulations! You won!";
        guessInput.disabled = true;
        guessBtn.disabled = true;
    }

    if (attempts === 0) {
        message.textContent = `😢 You lost! The word was: ${secretWord}`;
        guessInput.disabled = true;
        guessBtn.disabled = true;
    }

    guessInput.value = "";
});

restartBtn.addEventListener('click', startGame);

// Start game on page load
startGame();
