# Universal Keylogger | Python

A cross-platform keylogger designed for educational purposes. This script records keystrokes, clipboard content, screenshots, microphone audio, and system information—then encrypts and emails the data to a designated inbox.

---

## 📌 Features

- 🔑 Captures keyboard input using `pynput`
- 📋 Extracts clipboard contents via `pyperclip`
- 🖼️ Takes screenshots with `pyautogui`
- 🎙️ Records microphone input using `sounddevice`
- 💻 Logs system info like IP, OS, hostname, CPU
- 📩 Sends logs via email using `smtplib` (Gmail SMTP supported)
- 🔐 Encrypts data with `cryptography.fernet`
- 💻 Compatible with Linux, Windows, and macOS

---

## ⚙️ Tech Stack

- **Language:** Python 3.12+
- **Libraries:** `pynput`, `pyautogui`, `pyperclip`, `sounddevice`, `cryptography`, `requests`, `smtplib`, `scipy`, `Pillow`

---

## 🚀 How It Works

1. Collects and logs system, clipboard, keystroke, audio, and screenshot data.
2. Encrypts files using a Fernet key.
3. Sends all logs via Gmail (using a secure app password).
4. Operates cross-platform with platform-specific handling.

---

## 🔐 Gmail Setup

1. Enable 2-Step Verification on your Gmail.
2. Generate an [App Password](https://myaccount.google.com/apppasswords).
3. Replace placeholder credentials in the script:

```python
emailaddress = "your@gmail.com"
password = "your_app_password"  # NOT your Gmail login



🛠️ Setup & Usage
# Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required libraries
pip install -r requirements.txt

# Run the script
python Universal_Keylogger.py
Note: Add #!/path/to/venv/bin/python as the shebang if you want to run it directly.
