import csv
import math
import random
import pprint
import math

# SETUP
# ===
#
# (1,lambda) EA in HAMMING-BALL setting one OneMax and LeadingOnes

ns = [100, 250, 500]
funs = ["ONEMAX"]
repls = range(1, 101, 1)
setup_file = "data/study3.csv"

random.seed(123)

with open(setup_file, 'w', newline = '') as file:
  writer = csv.writer(file, delimiter = " ")
  writer.writerow(["jobid", "function", "n", "radius", "lambda", "maxevals", "repl", "seed"])
  i = 1
  for n in ns:
    for radius in [10, 20, 30]: #range(10, n+1, 5):
      for f in funs:
        for lam in range(1, 10 * math.ceil(math.log(n))):
          for repl in repls:
            seed = random.randint(1, 1000000)
            max_evals = 100 * n
            writer.writerow([i, f, n, radius, lam, max_evals, repl, seed])
            i += 1
