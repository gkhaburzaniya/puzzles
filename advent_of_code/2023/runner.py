import subprocess
import time

start = time.time()
subprocess.run(["python", "day_1.py"])
print(time.time() - start)
