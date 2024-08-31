import subprocess
import sys
import time

day = sys.argv[1]

start = time.time()
subprocess.run(["python", f"day_{day}.py"])
print(time.time() - start)
