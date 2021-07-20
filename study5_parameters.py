import csv
import math
import random
import pprint
import math

# SETUP
# ===
#
# (1+1) EA in RANDOM-OPTIMA setting one OneMax

ns = [100, 250, 500]
funs = ["ONEMAX"]
repls = range(1, 101, 1)
setup_file = "data/study5.csv"

random.seed(123)

with open(setup_file, 'w', newline = '') as file:
  writer = csv.writer(file, delimiter = " ")
  writer.writerow(["jobid", "function", "n", "ntargets", "repl", "seed"])
  i = 1
  for n in ns:
    for ntargets in range(0, n - 5 + 1, 5):
      for f in funs:
        for repl in repls:
          seed = random.randint(1, 1000000)
          writer.writerow([i, f, n, ntargets, repl, seed])
          i += 1
