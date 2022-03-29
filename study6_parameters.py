import csv
import math
import random
import pprint
import math

# SETUP
# ===
#
# (1+1) EA on PLATEAU with one/two additional target points

ns = range(10, 101, 10)
funs = ["PLATEAU", "RIDGE"]
targets = [0, 1, 2]
repls = range(1, 101, 1)
setup_file = "data/study6.csv"

random.seed(123)

with open(setup_file, 'w', newline = '') as file:
  writer = csv.writer(file, delimiter = " ")
  writer.writerow(["jobid", "function", "n", "ntargets", "repl", "seed"])
  i = 1
  for n in ns:
    for ntargets in targets:
      for f in funs:
        if (ntargets == 2) and (f == "RIDGE"):
          continue
        for repl in repls:
          seed = random.randint(1, 1000000)
          writer.writerow([i, f, n, ntargets, repl, seed])
          i += 1
