from EA.utils import *
import random
import math

# Terminate once minimal Hamming distance is reached
def termhd(target, r):
  def fn(x):
    return hammingd(x, target) <= r
  return fn

# Terminate once fitness is reached (or fitness level given by target explicitly)
def termf(target, f):
  def fn(x):
    return f(x) >= target
  return fn

# Terminate once optimum is reached OR a random point is found (approximately)
def termrnd(target, f, S):
  n = len(target)
  # if search point is passed: evaluate
  if len(target) > 1:
    target = f(target)
  searchspacesize = math.pow(2, n)
  lastx = None
  def fn(x):
    nonlocal lastx
    nonlocal S
    # compare with la
    if lastx is None:
      last = x
    elif last != x:
      last = x
      S -= 1
      S = math.max(S, 0)
    return ((f(x) == target) or (random.uniform(0, 1) < (S / searchspacesize)))
  return fn

# explicitly place targets
def termexplicit(targets):
  def fn(x):
    return (x in targets)
  return fn
