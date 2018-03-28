import subprocess
import time

while True:
    subprocess.run("git","pull")
    time.sleep(500)
