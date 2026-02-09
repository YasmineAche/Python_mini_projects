# 🔐 Password Manager & Generator
![Image of a lock](logo.png)

A secure, user-friendly password management application built with Python and Tkinter, following the MVC (Model-View-Controller) architectural pattern. The application helps users generate strong passwords, securely store their credentials in JSON format, search for saved passwords, and easily copy passwords to the clipboard.

![Python Version](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Storage JSON](https://img.shields.io/badge/Storage-JSON-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
---

## ✨ Features
### 🔑 Password Generation
- **Customizable Length:** Generate passwords with user-specified character count
- **Strong Security:** Includes uppercase, lowercase, digits, and special characters
- **Instant Generation:** Quick generation with customizable parameters
- **Clipboard Integration:** Automatic copying of generated password with confirmation

### 💾 Credential Management
- **JSON Storage:** Save website, email/username, and password combinations in structured JSON format
- **Organized Format:** Hierarchical data structure with website as key
- **Search Functionality:** Find saved credentials by website name 
- **Autofill Capability:** Found credentials automatically populate form fields

### 🔍 Search Features
- **Quick Search:** Find saved passwords by website name 
- **Auto-completion:** Retrieved data automatically fills email and password fields 
- **Error Handling:** Informative messages for found/not found searches

### 🎨 User Interface
- **Modern Design:** Clean, pink-themed interface with intuitive layout
- **Form Validation:** Ensures all fields are completed before saving
- **Confirmation Dialogs:** Double-check before saving sensitive data
- **Responsive Controls:** Well-aligned input fields and buttons
- **Clipboard Feedback:** Visual confirmation when passwords are copied
- **Search Integration:** Dedicated search button next to website field

---

## 📋 Prerequisites
- **Python 3.7** or higher
- **Required Python packages:**
  - Tkinter (usually included with Python installation)
  - pyperclip (for clipboard functionality)

---
## 🚀 Installation & Usage
1. Clone or download the project files
2. Ensure all files are in the same directory:
   - main.py - Application entry point
   - model.py - Data handling and password generation 
   - view.py - User interface components 
   - controller.py - Application logic 
   - logo.png - Application logo (optional)
3. Install Dependencie:
```bash
pip install pyperclip
```
4. Run the application:
```
python main.py
```
---
## 🏗️ Project Architecture
The application follows the **MVC pattern** for clean separation of concerns:

### Model (model.py)
- **JSON Storage:** Saves credentials in structured JSON format 
- **Password Generation:** Creates secure random passwords 
- **Search Function:** Retrieves data by website key 
- **File Management:** Creates and maintains user_data.json

### View (view.py)
- **GUI Components:** Creates and manages the graphical user interface 
- **Search Interface:** Dedicated search button integration 
- **Clipboard Operations:** Uses pyperclip for password copying 
- **Autofill:** Populates fields with found data 
- **Message Dialogs:** Confirmation and information messages

### Controller (controller.py)
- **Coordination:** Coordinates between Model and View
- **Event Coordination:** Connects button clicks to actions 
- **Search Logic:** Handles search requests and responses 
- **Validation:** Ensures data integrity before saving 
- **Flow Control:** Manages application state and user interactions

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
  - Generated password is automatically copied to clipboard

### 4. Save Credentials
- Click "Add" to save the entry
- Confirm details in the popup dialog
- Data saves to ```user_data.json```

### 5. Search for Saved Credentials
- Type website name in the "Website Link" field 
- Click the "Search" button next to it 
- If found:
  - Email/Username field autofills 
  - Password field autofills
- If not found: Information message appears


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
Credentials are saved in ```user_data.json``` with this structured format:
```
{
    "example.com": {
        "email/username": "user@example.com",
        "password": "P@ssw0rd123"
    },
    "github.com": {
        "email/username": "developer",
        "password": "Gh1bT0k3n$"
    }
}
```
---
## ⚠️ Security Notes
### Current Implementation
- **JSON Storage:** Credentials stored in plain JSON (not encrypted)
- **Clipboard Usage:** Passwords copied only during generation 
- **Search Security:** Retrieved passwords don't auto-copy to clipboard
- **Best For:** Personal, non-sensitive use on secure devices

---
## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

---
*Last Updated: Documentation reflects current implementation with JSON storage and search feature*