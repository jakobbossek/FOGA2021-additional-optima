import random as rnd

def rand_bs(n):
  return [rnd.randint(0, 1) for _ in range(n)]

def hammingd(x, y):
  return len([i for i in range(len(x)) if (x[i] != y[i])])
