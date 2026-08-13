# Guessing Game

A simple command-line number guessing game written in Python.

## Overview

This game chooses a random number and asks the player to guess it. After each guess the game reports whether the guess is too high, too low, or correct, and counts the number of attempts.

## Features

- Random number generation
- Input validation
- Attempt counter
- Helpful prompts and messages

## Requirements

- Python 3.7 or newer

## Installation

1. Clone the repository:

   git clone https://github.com/AVANI1001/guessing-game.git
   cd guessing-game

2. (Optional) Create and activate a virtual environment:

   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows

## Usage

Run the game with:

   python main.py

Follow the on-screen prompts to enter your guesses. The game will tell you whether each guess is too low, too high, or correct.

## Example

```
Welcome to the Guessing Game!
I'm thinking of a number between 1 and 100.
Enter your guess: 50
Too low. Try again.
Enter your guess: 75
Too high. Try again.
Enter your guess: 63
Correct! You guessed the number in 3 tries.
```

## Contributing

Contributions are welcome. Open an issue or submit a pull request with improvements or bug fixes.

## License

This project is provided under the MIT License. See LICENSE for details (if present).
