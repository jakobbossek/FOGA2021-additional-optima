import EA.EA
import EA.terminators
import EA.mutators
import EA.toyfuns
import math
import random
import sys
from EA.expsetup import read_setup

# SETUP
# ===
#
# (1+1) EA in RANDOM-OPTIMA setting one OneMax

setup_file = "data/study5.csv"

def run(jobid):
  setup = read_setup(setup_file, jobid)
  n = int(setup['n'])
  s = int(setup['ntargets']) # 2^s is the size of the random set
  jobid = int(setup['jobid'])
  f = getattr(EA.toyfuns, setup['function'])
  f = f()
  target = [1] * n

  random.seed(int(setup['seed']))

  term = EA.terminators.termrnd(target, f, math.pow(2, s))
  res = EA.EA.EA(lam = 1, n = n, f = f, term = term, mut = EA.mutators.mutunif, strategy = "plus")

  print("{} {}".format(jobid, res))

# pass first command line argument (the jobid)
run(sys.argv[1])
