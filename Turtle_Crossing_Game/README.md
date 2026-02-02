# 🐢 Turtle Crossing Game

A classic arcade-style turtle crossing game built with Python's **Turtle graphics library**.  
Help the turtle safely cross the busy road while avoiding moving cars!

![Python Version](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
---

## 📌 Table of Contents

- [Game Overview](#-game-overview)
- [Features](#-features)
- [Installation](#-installation)
- [How to Play](#-how-to-play)
- [Game Mechanics](#-game-mechanics)
- [Project Structure](#📁-project-structure)
- [License](#📝-license)

---

## 🎮 Game Overview

Control a turtle trying to cross a busy multi-lane road filled with colorful moving cars.  
Each successful crossing increases your level and the speed of the cars.  

**How many levels can you survive?**

---

## 🚀 Features

- **Simple Controls**: Use the spacebar to move the turtle forward
- **Progressive Difficulty**: Cars move faster with each level
- **Dynamic Car Generation**: Cars spawn in available lanes with random colors
- **Score Tracking**: Keep track of your current level
- **Visual Road Markings**: Realistic road lines for better immersion
- **Game Over Detection**: Collision detection with cars
- **Responsive Design**: Clean UI with instructions and score display

---

## 🛠️ Installation

### Clone the repository
```bash
git clone https://github.com/yourusername/turtle-crossing-game.git
cd turtle-crossing-game
```

### Requirements

- **Python 3.x**
- No additional dependencies required (uses built-in Turtle module)

### Run the game

```bash
python main.py
```

---

## 🎯 How to Play
- **Objective:** Guide the turtle from the bottom of the screen to the top without getting hit by cars.
- **Controls:** Press the Spacebar to move the turtle forward.
- **Winning:** Successfully reach the top of the screen to advance to the next level.
- **Losing:** Collide with any car to end the game.

---

## ⚙️ Game Mechanics
- **Car Spawning:** Cars randomly spawn in available lanes (1 in 6 chance each frame)
- **Speed Increment:** Each level increases car speed by 10 units
- **Lane Management:** 10 possible lanes for cars to occupy
- **Collision Detection:** Player loses if within 30 units of any car

---

## 📁 Project Structure
```bash
turtle-crossing-game/
│
├── main.py              # Main game loop and setup
├── player.py           # Player (Turtle) class
├── car_manager.py      # Car spawning and management
├── scoreboard.py       # Score tracking and road drawing
└── README.md           # This file
```
---

## 📝 License
This project is licensed under the [MIT License](LICENSE.md).