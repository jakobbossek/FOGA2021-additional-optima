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
# (1+1) EA in HAMMING-BALL setting one Jump_k

setup_file = "data/study2.csv"

def run(jobid):
  setup = read_setup(setup_file, jobid)
  n = int(setup['n'])
  k = int(setup['k'])
  jobid = int(setup['jobid'])
  radius = int(setup['radius'])
  f = getattr(EA.toyfuns, setup['function'])
  f = f(k) # JUMP_k
  target = [1] * n

  random.seed(int(setup['seed']))

  term = EA.terminators.termhd(target, r = radius)
  res = EA.EA.EA(lam = 1, n = n, f = f, term = term, mut = EA.mutators.mutunif, strategy = "plus")

  print("{} {}".format(jobid, res))

# pass first command line argument (the jobid)
run(sys.argv[1])
