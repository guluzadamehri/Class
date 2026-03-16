import math
n = int(input())
k = int(math.sqrt(n))
qaliq = n - k*k
say = 2*k*(k+1)
if qaliq > 0:
    say += 2*qaliq + 1
    if qaliq > k:
        say += 1
print(say)
