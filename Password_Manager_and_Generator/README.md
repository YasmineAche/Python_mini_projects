# 🔐 Password Manager & Generator
![Image of a lock](logo.png)

User-friendly password management application built with Python and Tkinter, following the MVC (Model-View-Controller) architectural pattern. The application helps users generate strong passwords and securely store their credentials.

![Python Version](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
---

## ✨ Features
### 🔑 Password Generation
- **Customizable Length:** Generate passwords with user-specified character count
- **Strong Security:** Includes uppercase, lowercase, digits, and special characters
- **Instant Generation:** Quick generation with customizable parameters
- **Clipboard Integration:** Automatic copying of generated passwords

### 💾 Credential Management
- **Secure Storage:** Save website, email/username, and password combinations
- **Organized Format:** Data stored in readable, columnar text format
- **Easy Retrieval:** Simple text-based storage for easy access
- **Clipboard Support:** Copy passwords directly to clipboard after generation

### 🎨 User Interface
- **Modern Design:** Clean, pink-themed interface with intuitive layout
- **Form Validation:** Ensures all fields are completed before saving
- **Confirmation Dialogs:** Double-check before saving sensitive data
- **Responsive Controls:** Well-aligned input fields and buttons

---
## 📋 Prerequisites
- **Python 3.7** or higher
- **Tkinter** (usually included with Python installation)

---
## 🚀 Installation & Usage
1. Clone or download the project files
2. Ensure all files are in the same directory:
   - main.py - Application entry point
   - model.py - Data handling and password generation 
   - view.py - User interface components 
   - controller.py - Application logic 
   - logo.png - Application logo (optional)
3. Run the application:
```
python main.py
```
---
## 🏗️ Project Architecture
The application follows the MVC pattern for clean separation of concerns:

### Model (model.py)
- Handles data persistence and file operations
- Implements password generation algorithms
- Manages the credentials text file

### View (view.py)
- Creates and manages the graphical user interface
- Handles user input and display
- Manages dialog boxes and message displays

### Controller (controller.py)
- Coordinates between Model and View
- Handles button click events
- Manages application flow and validation
---
## 🎯 How to Use
### 1. Enter Website Information
- Type the website URL in the "Website Link" field
- The cursor automatically focuses here for quick entry

### 2. Enter Email/Username
- Type your email or username
- Defaults to "@gmail.com" for convenience (editable)

### 3. Generate or Enter Password
- Option A: Type your own password
- Option B: Click "Generate Password" to create a secure password
  - A dialog will ask for desired password length 
  - Default is 8 characters, customizable

### 4. Save Credentials
- Click "Add" to save the entry
- Confirm details in the popup dialog
- Data saves to ```user_data.txt```
---
## 📁 File Structure
```
password-manager/
├── main.py              # Application entry point
├── model.py            # Data model & password generation
├── view.py             # GUI components
├── controller.py       # Application controller
├── logo.png           # Application logo
├── user_data.txt      # Generated credentials file (auto-created)
└── README.md          # This documentation
```
---
## 📊 Data Storage Format
Credentials are saved in user_data.txt with this format:
```
Website | Email/Username | Password
-----------------------------------
google.com | user@gmail.com | P@ssw0rd!
github.com | developer | Gh1bT0k3n$
```
---
## ⚠️ Security Notes
### Current Implementation
- Passwords are stored in plain text in user_data.txt
- No encryption is applied to stored data
- Suitable for personal, non-sensitive use only
---
## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.