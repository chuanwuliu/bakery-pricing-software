import time
import numpy as np
from matplotlib import pyplot as plt
from software.algos import greedy_allocate, exhaustive_allocate

m = np.linspace(1, 500, 10)
t_list_greedy = []
t_list_exhust = []

for mi in m:

    t0 = time.time()
    greedy_allocate(int(mi), [8, 5, 2])
    t = time.time() - t0
    t_list_greedy.append(t)

    t0 = time.time()
    exhaustive_allocate(int(mi), [8, 5, 2])
    t = time.time() - t0
    t_list_exhust.append(t)

plt.figure(figsize=(8, 4))
plt.title('Greedy approximation vs exhaustive search')
plt.plot(m, t_list_greedy, 'o-', label='Greedy method')
plt.plot(m, t_list_exhust, 's-', label='Exhaustive method')
plt.xlabel('Number of Order')
plt.ylabel('Rum time [seconds]')
plt.legend()
plt.savefig('comparison.pdf')
plt.show()

