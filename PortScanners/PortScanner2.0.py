import socket
import threading
from queue import Queue
import warnings
import time
import argparse

# Start timer to measure how long the port scan takes
start = time.time()

# Suppress socket-related warnings
warnings.simplefilter("ignore")

# Prompt user for the target IP address
print()
target = input("Enter in IP address like -> (127.0.0.1): ")
print()

# Initialize a thread-safe queue for port numbers and a list to hold open ports
queue = Queue()
openPorts = []

# Basic TCP port scanner using SOCK_STREAM (TCP)
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target, port))
        sock.close()
        return True
    except:
        return False

# Attempt to retrieve service/banner information from an open port
def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return "No banner"

# Fill the queue with port numbers to scan
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

# Worker function for each thread: pulls ports from the queue, scans them, and grabs banners
def backend():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            banner = grab_banner(target, port)
            print(f"[+] Port {port} is open | Banner: {banner}")
            openPorts.append((port, banner))

# Define the range of ports to scan (1 through 65534)
port_list = range(1, 65535)
fill_queue(port_list)

# Create and start threads
thread_list = []
for t in range(100):  # Number of threads to run concurrently
    threads = threading.Thread(target=backend)
    thread_list.append(threads)

# Start all threads
for thread in thread_list:
    thread.start()

# Wait for all threads to complete
for thread in thread_list:
    thread.join()

# Print the list of open ports with their banners
print("Open ports are: ", openPorts)

# Calculate and print total scan duration
end = time.time()
print(f"Time taken: {end - start:.4f} seconds")
