let flashcards = [];
let currentIndex = 0;

async function loadFlashcards() {
    const res = await fetch('/get_flashcards');
    flashcards = await res.json();
    currentIndex = 0;
    showFlashcard();
}

function showFlashcard() {
    const container = document.getElementById('flashcard-container');
    container.innerHTML = '';

    if (currentIndex >= flashcards.length) {
        container.innerHTML = '<p>You completed all flashcards!</p>';
        return;
    }

    const card = document.createElement('div');
    card.className = 'flashcard';

    const imgHTML = flashcards[currentIndex].image
        ? `<img src="/static/${flashcards[currentIndex].image}" alt="">`
        : '';

    card.innerHTML = `
        <div class="front">
            ${imgHTML}
            <p>${flashcards[currentIndex].question}</p>
        </div>
        <div class="back">
            <p>${flashcards[currentIndex].answer}</p>
            <p2>${flashcards[currentIndex].answer2}</p2>
            <p3>${flashcards[currentIndex].answer3}</p3>
        </div>
    `;


    card.addEventListener('click', () => {
        card.classList.toggle('flip');
    });

    container.appendChild(card);
}

document.getElementById('next-btn').addEventListener('click', () => {
    currentIndex++;
    showFlashcard();
});

loadFlashcards();