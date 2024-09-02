import subprocess
import sys
import time

pypy_days = {11, 16}

day = int(sys.argv[1])

runner = "pypy" if day in pypy_days else "python"

start = time.time()
subprocess.run([runner, f"day_{day}.py"])
print(f"Day: {day} {runner}: {time.time() - start}")
