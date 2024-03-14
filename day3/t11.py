import math
import time
start_time = time.time()
PI = 0
i = 1
while abs(PI * 4 - math.pi) >= 1e-8:
    PI += pow(-1, i + 1) / (2 * i - 1)
    i += 1
print("PI", PI * 4)
print("循环次数", i)
print(time.time() - start_time, "s")
