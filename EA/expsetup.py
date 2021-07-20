def read_setup(setupfile, jobid):
  '''
  Read setup parameters from file.
  jobid is the line number. Additionally the first line is read. It contains the
  parameter names. Return value is a dict with the names as keys and the string
  parameters as values.
  '''
  with open(setupfile, 'r') as f:
    lines = [x for i, x in enumerate(f) if i in [0, int(jobid)]]
    lines = [line.strip("\n").split(' ') for line in lines]
    assert(len(lines) == 2)
    return dict(zip(lines[0], lines[1]))
