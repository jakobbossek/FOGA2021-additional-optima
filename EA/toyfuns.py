import random as rnd
import math

# ONEMAX
def ONEMAX():
  def fn(x):
    return sum(x)
  return fn

def ZEROMAX():
  def fn(x):
    return len(x) - sum(x)
  return fn

# LEADING-ONES
def LO():
  def fn(x):
    n = len(x)
    s = 0
    for i in range(n):
      if x[i] == 0:
        return s
      s += 1
    return s
  return fn

# JUMP_k
def JUMP(k):
  def fn(x):
    n = len(x)
    s = sum(x)
    if s <= (n - k) or s == n:
      return k + s
    return n - s
  return fn

# TRAP
def TRAP():
  def fn(x):
    s = sum(x)
    if s == 0:
      return len(x) + 1
    return s
  return fn

def SPC():
  def fn(x):
    # Definition 5 in https://eldorado.tu-dortmund.de/bitstream/2003/5398/1/ci96.pdf
    n = len(x)
    s = sum(x)
    # Case 1
    if s == n:
      return 2 * n

    # Case 2
    u = 0
    for i in range(n):
      if x[i] == 0:
        break
      else:
        u += 1
    # first s bits are 1, others are necessarily 0
    if s == u:
      return n

    # Case 3
    return n - s
  return fn

def SPI():
  def fn(x):
    # Definition 3 in https://eldorado.tu-dortmund.de/bitstream/2003/5398/1/ci96.pdf
    n = len(x)
    s = sum(x)

    # Case 1
    if s == n:
      return 2 * n

    # Case 2
    u = 0
    j = 0
    for i in range(n):
      if x[i] == 0:
        break
      else:
        u += 1
        j += 1
    # first s bits are 1, others are necessarily 0
    if s == u:
      # 0 < eps_j = n * ((1 / (n + 1)) * (j + 1)) < n with eps_j < eps_{j+1}
      return n + n * ((1 / (n + 1)) * (j + 1))

    # Case 3
    return n - s

  return fn


# Ridge is an alias for SPI
def RIDGE():
  return SPI()
