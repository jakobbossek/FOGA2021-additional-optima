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

setup_file = "data/study6.csv"

def run(jobid):
  setup = read_setup(setup_file, jobid)
  n = int(setup['n'])
  ntargets = int(setup['ntargets']) # either on or two
  jobid = int(setup['jobid'])
  f = getattr(EA.toyfuns, setup['function'])
  f = f()

  # see Thm. 5.3 in paper
  nsq = math.ceil(math.sqrt(n))
  s1 = ([1] * nsq) + ([0] * (n - nsq))
  s2 = ([1] * (nsq + 1)) + ([0] * (n - nsq - 1))
  opt = [1] * n
  S = []
  if ntargets == 0:
    S = [opt]
  elif ntargets == 1:
    S = [opt, s1]
  else:
    S = [opt, s1, s2]

  random.seed(int(setup['seed']))

  term = EA.terminators.termexplicit(S)
  res = EA.EA.EA(lam = 1, n = n, f = f, term = term, mut = EA.mutators.mutunif, strategy = "plus")

  print("{} {}".format(jobid, res))

# pass first command line argument (the jobid)
run(sys.argv[1])
