import random as rnd

def mutunif(x):
  n = len(x)
  y = x[:]
  p = 1/n
  for i in range(n):
    if rnd.uniform(0, 1) < p:
      y[i] = 1 - y[i]
  return y
