# 🍅 Pomodoro Timer App
![Image of a tomato](tomato.png)

A simple, elegant Pomodoro timer application built with Python and Tkinter, following the MVC (Model-View-Controller) architectural pattern.

![Python Version](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
---

## Table of Contents
- [Features](#1-features)
- [How It Works](#2-how-it-works)
- [Requirements](#3-requirements)
- [Project Structure](#4-project-structure)
- [UI Components](#5-ui-components)
- [Sound Support](#6-sound-support)
- [Architecture](#7-architecture)
- [License](#8-license)

---
## 1. Features

- **Pomodoro Technique Implementation:** 25-minute work sessions followed by 5-minute short breaks
- **Cycle Management:** Automatic session switching (Work → Short Break → Work → Long Break)
- **Visual Feedback:**
  - Tomato-themed interface with color-coded sessions 
  - Progress tracking with checkmarks 
  - Clear session type indicators
- **Sound Notifications:** Platform-specific sound alerts when sessions end (needs improvement)
- **Responsive Controls:** Start and reset functionality

---

## 2. How It Works

The app follows the standard Pomodoro technique:

1. **Work Session:** 25 minutes of focused work
2. **Short Break:** 5 minutes of rest (after each work session)
3. **Long Break:** 20 minutes of rest (after 4 work sessions)
4. **Cycle repeats** automatically

---

## 3. Requirements

- Python 3.7 or higher
- Tkinter (usually comes with Python)

---

## 4. Project Structure
```
Pomodoro/
├── main.py              # Application entry point
├── controller.py        # Controller (business logic)
├── model.py            # Model (data and calculations)
├── view.py             # View (GUI components)
├── tomato.png          # Tomato image for UI
└── README.md           # This file
```

---

## 5. UI Components
- **Timer Display:** Large countdown timer in the center
- **Session Title:** Shows current session type (Work/Break/Timer)
- **Checkmarks:** Visual progress indicator (✔ for completed work sessions)
- **Control Buttons:**
  - **Start:** Begins the countdown 
  - **Reset:** Returns to initial state

---

## 6. Sound Support
The app provides platform-specific sound notifications:
- **Windows:** Uses winsound.Beep() for system beeps
- **macOS:** Uses afplay with system sounds (Ping.aiff)
- **Linux:** No sound

---

## 7. Architecture
This application follows the MVC pattern:
- **Model (model.py):** Manages application data and Pomodoro logic
    - Time calculations 
    - Session state management 
    - Business rules implementation
- **View (view.py):** Handles the user interface 
  - Tkinter widgets and layout 
  - Visual updates and styling 
  - User input handling
- **Controller (controller.py):** Coordinates between Model and View
  - Event handling 
  - Timer management 
  - Sound notifications 
  - Application flow control

---

## 8. License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.