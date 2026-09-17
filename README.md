# 🔢 Python Number Guessing Game (with High Score Tracker)

A Python terminal-based number guessing game featuring dynamic random number generation, persistent high-score file storage (`hi-score.txt`), and automated streak tracking.

## 📸 Terminal Output
```text
Enter your guess between 1 to 5: 3
Your Guess: 3, Computer Guess: 3
You won
Enter your guess between 1 to 5: 1
Your Guess: 1, Computer Guess: 2
You lose
Final score: 1
Highscore: 2
```

## 🛠️ Key Technical Features
- Dynamic Randomization: Utilizes Python's native random module to generate random integers between 1 and 5 for each round.

- Persistent File Storage (I/O): Reads and writes game performance data to a local hiscore.txt file to save high scores permanently across sessions.

- Game Loop Logic: Features an interactive loop that keeps the match running on successful guesses and terminates cleanly on an incorrect answer.

- Score Tracking Engine: Calculates your current streak in real-time and compares it against the saved high score upon game over.

## 🧰 Tech Stack
- Python 3

- Python File I/O (open(), read(), write())

- random module
