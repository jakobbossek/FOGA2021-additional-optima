import csv
import math
import random
import pprint
from itertools import product

# SETUP
# ===
#
# (1+1) EA in HAMMING-BALL setting one Jump_k

ns = [30]
funs = ["JUMP"]
ks = [2, 3, 4]
repls = range(1, 101, 1)
setup_file = "data/study2.csv"

random.seed(123)

with open(setup_file, 'w', newline = '') as file:
  writer = csv.writer(file, delimiter = " ")
  writer.writerow(["jobid", "function", "n", "k", "radius", "repl", "seed"])
  i = 1
  for n in ns:
    for k in ks:
      for radius in range(k+1):
        for f in funs:
          for repl in repls:
            seed = random.randint(1, 1000000)
            writer.writerow([i, f, n, k, radius, repl, seed])
            i += 1
