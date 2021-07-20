import csv
import math
import random
import pprint
import math

# SETUP
# ===
#
# (1+1) EA in FITNESS-LEVEL-MERGING setting one OneMax and LeadingOnes

ns = [100, 250, 500]
funs = ["ONEMAX", "LO"]
repls = range(1, 11, 1)
setup_file = "data/study4.csv"

random.seed(123)

with open(setup_file, 'w', newline = '') as file:
  writer = csv.writer(file, delimiter = " ")
  writer.writerow(["jobid", "function", "n", "level", "repl", "seed"])
  i = 1
  for n in ns:
    for level in range(1, n + 1, 5):
      for f in funs:
        for repl in repls:
          seed = random.randint(1, 1000000)
          writer.writerow([i, f, n, level, repl, seed])
          i += 1
