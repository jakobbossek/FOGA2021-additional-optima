import EA.EA
import EA.terminators
import EA.mutators
import EA.toyfuns
import math
import random
import sys
# from joblib import Parallel, delayed # pip install joblib
# import multiprocessing
from EA.expsetup import read_setup

# SETUP
# ===
#
# (1+1) EA in HAMMING-BALL setting one OneMax and LeadingOnes

setup_file = "data/study1.csv"

def run(jobid):
  setup = read_setup(setup_file, jobid)
  jobid = int(setup['jobid'])
  n = int(setup['n'])
  radius = int(setup['radius'])
  f = getattr(EA.toyfuns, setup['function'])
  f = f()
  target = [1] * n

  random.seed(int(setup['seed']))

  term = EA.terminators.termhd(target, r = radius)
  res = EA.EA.EA(lam = 1, n = n, f = f, term = term, mut = EA.mutators.mutunif, strategy = "plus")

  print("{} {}".format(jobid, res))

# pass first command line argument (the jobid)
run(sys.argv[1])

# if __name__ == "__main__":
#   with open(setup_file, newline = '') as setupfile:
#     reader = csv.DictReader(setupfile, delimiter = ' ')
#     n_cpus = multiprocessing.cpu_count()
#     print("Starting experiments on {0} cores...\n".format(n_cpus))
#     Parallel(n_jobs = n_cpus)(delayed(run)(row) for row in reader)
