import subprocess
import psutil

def change_process_name(pid, new_name):
    try:
        process = psutil.Process(pid)
        process.name() == new_name
    except psutil.NoSuchProcess:
        print("Process not found.")

def run_bot():
    process = subprocess.Popen(["python", "ZUwy1d6t8K.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
    return process.pid

if __name__ == "__main__":
    pid = run_bot()
    change_process_name(pid, "New Process Name")