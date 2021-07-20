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
# (1+1) EA in FITNESS-LEVEL-MERGING setting one OneMax and LeadingOnes

setup_file = "data/study4.csv"

def run(jobid):
  setup = read_setup(setup_file, jobid)
  n = int(setup['n'])
  jobid = int(setup['jobid'])
  level = int(setup['level']) # fitnes level, i.e. minimum target value
  f = getattr(EA.toyfuns, setup['function'])
  f = f()

  random.seed(int(setup['seed']))

  term = EA.terminators.termf(level, f)
  res = EA.EA.EA(lam = 1, n = n, f = f, term = term, mut = EA.mutators.mutunif, strategy = "plus")

  print("{} {}".format(jobid, res))

# pass first command line argument (the jobid)
run(sys.argv[1])
