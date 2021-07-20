import csv
import math
import random
import pprint
from itertools import product

# SETUP
# ===
#
# (1+1) EA in HAMMING-BALL setting one OneMax and LeadingOnes

ns = [100, 250, 500]
funs = ["ONEMAX", "LO"]
repls = range(1, 101, 1)
setup_file = "data/study1.csv"

random.seed(123)

with open(setup_file, 'w', newline = '') as file:
  writer = csv.writer(file, delimiter = " ")
  writer.writerow(["jobid", "function", "n", "radius", "repl", "seed"])
  i = 1
  for n in ns:
    for radius in range(10, n+1, 5):
      for f in funs:
        for repl in repls:
          seed = random.randint(1, 1000000)
          writer.writerow([i, f, n, radius, repl, seed])
          i += 1
