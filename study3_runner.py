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
# (1,lambda) EA in HAMMING-BALL setting one OneMax and LeadingOnes


setup_file = "data/study3.csv"

def run(jobid):
  setup = read_setup(setup_file, jobid)
  n = int(setup['n'])
  jobid = int(setup['jobid'])
  radius = int(setup['radius'])
  lam = int(setup['lambda'])
  maxevals = int(setup['maxevals'])
  f = getattr(EA.toyfuns, setup['function'])
  f = f()
  target = [1] * n

  random.seed(int(setup['seed']))

  term = EA.terminators.termhd(target, r = radius)
  res = EA.EA.EA(lam = lam, n = n, f = f, term = term, maxevals = maxevals, mut = EA.mutators.mutunif, strategy = "comma")

  print("{} {}".format(jobid, res))

# pass first command line argument (the jobid)
run(sys.argv[1])
