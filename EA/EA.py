from EA.utils import *

def EA(lam, n, f, term, mut, strategy = "plus", maxevals = float('inf')):
  x = rand_bs(n)
  fx = f(x)
  fevals = 1

  while not term(x) and fevals < maxevals:
    # list of lists
    O = [mut(x) for _ in range(lam)]
    # >> fix
    if any(map(term, O)):
      break
    # << fix
    fO = list(map(f, O))
    Obestidx = fO.index(max(fO))
    if strategy == "comma":
      x = O[Obestidx]
      fx = fO[Obestidx]
    else:
      if fO[Obestidx] >= fx:
        x = O[Obestidx]
        fx = fO[Obestidx]
    fevals += lam

  return fevals

if __name__ == '__main__':
  n = 100
  target = [1] * n
  term = termhd(target, r = 0)
  res = EA(lam = 1, n = 100, f = ONEMAX, term = term, mut = mutunif, strategy = "plus")
  print("fevals: {}, nlog(n): {}", res, 2.71 * n * math.log(n))
