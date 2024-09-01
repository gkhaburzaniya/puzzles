import subprocess
import time

pypy_days = [11, 16]

for day in range(1, 17):
    start = time.time()
    subprocess.run(["python3.12", f"day_{day}.py"])
    print(f"Day: {day} python3.12: {time.time() - start}")
    start = time.time()
    subprocess.run(["pypy", f"day_{day}.py"])
    print(f"Day: {day} pypy: {time.time() - start}")
