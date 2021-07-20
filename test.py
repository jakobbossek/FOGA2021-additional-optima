import EA.EA
import EA.terminators
import EA.mutators
import EA.toyfuns
import math

if __name__ == "__main__":
  n = 100
  target = [1] * n
  f = EA.toyfuns.ONEMAX()
  term = EA.terminators.termrnd(target, f, S = math.pow(2, 50))
  res = EA.EA.EA(lam = 1, n = n, f = f, term = term, mut = EA.mutators.mutunif, strategy = "plus")
  print("fevals: {}, nlog(n): {}", res, 2.71 * n * math.log(n))
